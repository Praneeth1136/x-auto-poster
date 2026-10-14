import os
import sys
import tweepy

client = tweepy.Client(
    consumer_key=os.environ["X_API_KEY"],
    consumer_secret=os.environ["X_API_SECRET"],
    access_token=os.environ["X_ACCESS_TOKEN"],
    access_token_secret=os.environ["X_ACCESS_SECRET"]
)

with open("posts.txt", "r", encoding="utf-8") as f:
    content = f.read().strip()

if not content:
    print("Queue is empty! Add more posts to posts.txt.")
    sys.exit(0)

posts = [p.strip() for p in content.split("---") if p.strip()]

if not posts:
    print("No valid posts found.")
    sys.exit(0)

current_post = posts[0]
response = client.create_tweet(text=current_post)
print(f"Successfully published Tweet ID: {response.data['id']}")

remaining_posts = "\n---\n".join(posts[1:])
with open("posts.txt", "w", encoding="utf-8") as f:
    f.write(remaining_posts + ("\n" if remaining_posts else ""))
