#!/usr/bin/env python3
"""
Fetch recent tweets via X GraphQL API using session cookies (no API key needed).
Usage: python3 fetch-tweets.py handle1 handle2 ...
Env:   TWITTER_COOKIES — "auth_token=xxx; ct0=yyy"
Output: JSON array to stdout
"""

import json
import os
import sys
import time
from datetime import datetime, timezone, timedelta

import httpx

LOOKBACK_DAYS = 30
MAX_TWEETS = 3
BEARER = "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
GQL = "https://x.com/i/api/graphql"

FEATURES = {
    "articles_preview_enabled": False,
    "c9s_tweet_anatomy_moderator_badge_enabled": True,
    "communities_web_enable_tweet_community_results_fetch": True,
    "creator_subscriptions_quote_tweet_preview_enabled": False,
    "creator_subscriptions_tweet_preview_api_enabled": True,
    "freedom_of_speech_not_reach_fetch_enabled": True,
    "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
    "longform_notetweets_consumption_enabled": True,
    "longform_notetweets_inline_media_enabled": True,
    "longform_notetweets_rich_text_read_enabled": True,
    "responsive_web_edit_tweet_api_enabled": True,
    "responsive_web_enhance_cards_enabled": False,
    "responsive_web_graphql_exclude_directive_enabled": True,
    "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
    "responsive_web_graphql_timeline_navigation_enabled": True,
    "responsive_web_grok_analyze_button_fetch_trends_enabled": False,
    "responsive_web_grok_analyze_post_followups_enabled": False,
    "responsive_web_grok_analysis_button_from_backend": False,
    "responsive_web_grok_image_annotation_enabled": False,
    "responsive_web_grok_share_attachment_enabled": False,
    "responsive_web_grok_show_grok_translated_post": True,
    "responsive_web_jetfuel_frame": False,
    "responsive_web_media_download_video_enabled": False,
    "responsive_web_twitter_article_tweet_consumption_enabled": True,
    "rweb_tipjar_consumption_enabled": True,
    "rweb_video_screen_enabled": True,
    "rweb_video_timestamps_enabled": True,
    "standardized_nudges_misinfo": True,
    "tweet_awards_web_tipping_enabled": False,
    "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
    "tweet_with_visibility_results_prefer_gql_media_interstitial_enabled": False,
    "tweetypie_unmention_optimization_enabled": True,
    "verified_phone_label_enabled": False,
    "view_counts_everywhere_api_enabled": True,
    "premium_content_api_read_enabled": False,
    "profile_label_improvements_pcf_label_in_post_enabled": False,
}


def parse_cookies(s):
    out = {}
    for part in s.split("; "):
        if "=" in part:
            k, v = part.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def make_client(cookies):
    ct0 = cookies.get("ct0", "")
    return httpx.Client(
        cookies=cookies,
        headers={
            "Authorization": f"Bearer {BEARER}",
            "X-Csrf-Token": ct0,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json",
            "Referer": "https://x.com/",
            "Origin": "https://x.com",
            "x-twitter-active-user": "yes",
            "x-twitter-auth-type": "OAuth2Session",
            "x-twitter-client-language": "en",
        },
        timeout=20.0,
        follow_redirects=True,
    )


def get_user(client, handle):
    params = {
        "variables": json.dumps({"screen_name": handle, "withSafetyModeUserFields": True}),
        "features": json.dumps({
            "hidden_profile_subscriptions_enabled": True,
            "rweb_tipjar_consumption_enabled": True,
            "responsive_web_graphql_exclude_directive_enabled": True,
            "verified_phone_label_enabled": False,
            "highlights_tweets_tab_ui_enabled": True,
            "responsive_web_twitter_article_notes_tab_enabled": True,
            "creator_subscriptions_tweet_preview_api_enabled": True,
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
            "responsive_web_graphql_timeline_navigation_enabled": True,
        }),
        "fieldToggles": json.dumps({"withAuxiliaryUserLabels": False}),
    }
    r = client.get(f"{GQL}/G3KGOASz96M-Qu0nwmGXNg/UserByScreenName", params=params)
    if r.status_code != 200:
        print(f"UserByScreenName {handle}: HTTP {r.status_code}", file=sys.stderr)
        return None
    result = r.json().get("data", {}).get("user", {}).get("result", {})
    if not result:
        return None
    legacy = result.get("legacy", {})
    return {"id": result.get("rest_id", ""), "name": legacy.get("name", handle), "bio": legacy.get("description", "")}


def get_tweets(client, user_id, handle, cutoff):
    params = {
        "variables": json.dumps({
            "userId": user_id, "count": 20, "includePromotedContent": False,
            "withQuickPromoteEligibilityTweetFields": True, "withVoice": True, "withV2Timeline": True,
        }),
        "features": json.dumps(FEATURES),
        "fieldToggles": json.dumps({"withArticlePlainText": False}),
    }
    r = client.get(f"{GQL}/HeWHY26ItCfUmm1e6ITjeA/UserTweets", params=params)
    if r.status_code != 200:
        print(f"UserTweets {handle}: HTTP {r.status_code}", file=sys.stderr)
        return []

    body = r.json()
    user_result = body.get("data", {}).get("user", {}).get("result", {})
    tl_root = user_result.get("timeline_v2") or user_result.get("timeline") or {}
    instructions = tl_root.get("timeline", tl_root).get("instructions", [])

    entries = []
    for instr in instructions:
        if instr.get("type") == "TimelineAddEntries":
            entries = instr.get("entries", [])
            break

    tweets = []
    for entry in entries:
        item = entry.get("content", {}).get("itemContent", {})
        if item.get("itemType") != "TimelineTweet":
            continue
        tweet_result = item.get("tweet_results", {}).get("result", {})
        if tweet_result.get("__typename") == "TweetWithVisibilityResults":
            tweet_result = tweet_result.get("tweet", {})
        legacy = tweet_result.get("legacy", {})
        if not legacy:
            continue
        if legacy.get("retweeted_status_result") or legacy.get("in_reply_to_status_id_str"):
            continue
        text = legacy.get("full_text", "")
        if text.startswith("RT @"):
            continue
        try:
            created = datetime.strptime(legacy["created_at"], "%a %b %d %H:%M:%S +0000 %Y").replace(tzinfo=timezone.utc)
        except Exception:
            continue
        if created < cutoff:
            continue
        for url_obj in legacy.get("entities", {}).get("urls", []):
            short = url_obj.get("url", "")
            expanded = url_obj.get("expanded_url", short)
            if short:
                text = text.replace(short, expanded)
        tid = legacy.get("id_str", "")
        tweets.append({
            "id": tid, "text": text, "createdAt": created.isoformat(),
            "url": f"https://x.com/{handle}/status/{tid}",
            "likes": legacy.get("favorite_count", 0),
            "retweets": legacy.get("retweet_count", 0),
            "replies": legacy.get("reply_count", 0),
        })
        if len(tweets) >= MAX_TWEETS:
            break
    return tweets


def main():
    handles = sys.argv[1:]
    if not handles:
        print("[]")
        return

    cookie_str = os.environ.get("TWITTER_COOKIES", "")
    if not cookie_str:
        print(json.dumps({"error": "TWITTER_COOKIES not set"}), file=sys.stderr)
        print("[]")
        return

    cookies = parse_cookies(cookie_str)
    cutoff = datetime.now(timezone.utc) - timedelta(days=LOOKBACK_DAYS)
    results = []

    with make_client(cookies) as client:
        for handle in handles:
            try:
                user = get_user(client, handle)
                if not user:
                    print(f"Skipping @{handle}: user not found", file=sys.stderr)
                    time.sleep(1)
                    continue
                tweets = get_tweets(client, user["id"], handle, cutoff)
                if tweets:
                    results.append({"handle": handle, "name": user["name"], "bio": user["bio"], "tweets": tweets})
                    print(f"@{handle}: {len(tweets)} tweets", file=sys.stderr)
                else:
                    print(f"@{handle}: no recent tweets", file=sys.stderr)
                time.sleep(1.5)
            except Exception as e:
                print(f"Error @{handle}: {e}", file=sys.stderr)
                time.sleep(3)

    print(json.dumps(results, ensure_ascii=False))


if __name__ == "__main__":
    main()
