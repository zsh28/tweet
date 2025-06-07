from datetime import datetime, timezone
from textblob import TextBlob
from src.trusted_accounts import fetch_trusted_accounts

def analyze_account(client, user):
    now = datetime.now(timezone.utc)
    created_at = user.created_at
    age_years = round((now - created_at).days / 365, 2)

    followers = user.public_metrics["followers_count"]
    following = user.public_metrics["following_count"]
    ratio = round(followers / following, 2) if following else followers

    bio = user.description or "No bio."

    # Trusted account check
    trusted_ids = fetch_trusted_accounts()
    trusted_followed = 0

    try:
        following_response = client.get_users_following(id=user.id, max_results=1000)
        if following_response.data:
            following_ids = [u.id for u in following_response.data]
            trusted_followed = len(set(trusted_ids).intersection(set(following_ids)))
    except Exception as e:
        print("⚠️ Could not fetch following list:", e)

    # Get recent tweets
    tweets = client.get_users_tweets(id=user.id, max_results=10, tweet_fields=["public_metrics"])
    likes = 0
    rts = 0
    sentiments = []

    if tweets.data:
        for t in tweets.data:
            metrics = t.public_metrics or {}
            likes += metrics.get("like_count", 0)
            rts += metrics.get("retweet_count", 0)
            sentiments.append(TextBlob(t.text).sentiment.polarity)

    avg_likes = likes // len(tweets.data) if tweets.data else 0
    avg_rts = rts // len(tweets.data) if tweets.data else 0
    avg_sentiment = round(sum(sentiments) / len(sentiments), 2) if sentiments else 0

    return {
        "age_years": age_years,
        "ratio": ratio,
        "bio": bio,
        "avg_likes": avg_likes,
        "avg_rts": avg_rts,
        "trusted_count": trusted_followed,
        "sentiment": avg_sentiment
    }
