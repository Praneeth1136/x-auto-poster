#!/usr/bin/env python3
"""
X (Twitter) Auto Poster Bot
Dispatches the first pending post from posts.txt using Tweepy API v2.
"""

import os
import sys
import tweepy

def main():
    required_keys = ["X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_SECRET"]
    missing = [k for k in required_keys if not os.environ.get(k)]
    if missing:
        print(f"Error: Missing required environment variables: {', '.join(missing)}")
        sys.exit(1)

    client = tweepy.Client(
        consumer_key=os.environ["X_API_KEY"],
        consumer_secret=os.environ["X_API_SECRET"],
        access_token=os.environ["X_ACCESS_TOKEN"],
        access_token_secret=os.environ["X_ACCESS_SECRET"]
    )

    if not os.path.exists("posts.txt"):
        print("Error: posts.txt file not found.")
        sys.exit(1)

    with open("posts.txt", "r", encoding="utf-8") as f:
        content = f.read().strip()

    if not content:
        print("Queue is empty! Add more posts to posts.txt.")
        sys.exit(0)

    posts = [p.strip() for p in content.split("---") if p.strip()]

    if not posts:
        print("No valid posts found in queue.")
        sys.exit(0)

    current_post = posts[0]
    try:
        response = client.create_tweet(text=current_post)
        print(f"Successfully published Tweet ID: {response.data['id']}")
    except tweepy.TweepyException as err:
        print(f"Failed to publish tweet: {err}")
        sys.exit(1)

    remaining_posts = "\n---\n".join(posts[1:])
    with open("posts.txt", "w", encoding="utf-8") as f:
        f.write(remaining_posts + ("\n" if remaining_posts else ""))

if __name__ == "__main__":
    main()
