# X (Twitter) Auto Poster

Automated post dispatcher that reads scheduled content from `posts.txt` and publishes updates to X (formerly Twitter) using the Twitter API v2.

---

## Features
- **Queue-Based Scheduling:** Posts are separated by `---` in `posts.txt` and consumed FIFO.
- **State Persistence:** Automatically removes published entries after successful dispatch.
- **GitHub Actions Integration:** Triggered periodically via cron workflow in `.github/workflows/schedule.yml`.

## Prerequisites
- Python 3.10+
- Tweepy library: `pip install tweepy`
- Twitter Developer App credentials (API Key, API Secret, Access Token, Access Token Secret)

## Environment Variables
| Variable | Description |
| :--- | :--- |
| `X_API_KEY` | OAuth 1.0a Consumer Key |
| `X_API_SECRET` | OAuth 1.0a Consumer Secret |
| `X_ACCESS_TOKEN` | OAuth 1.0a User Access Token |
| `X_ACCESS_SECRET` | OAuth 1.0a User Access Secret |
