from src.analyzer import analyze_account
from src.reply_engine import send_reply

def process_mentions(client, since_id):
    query = '"riddle me this" is:reply -is:retweet'
    tweets = client.search_recent_tweets(
        query=query,
        since_id=since_id,
        tweet_fields=["author_id", "in_reply_to_user_id", "conversation_id", "referenced_tweets", "public_metrics", "created_at"],
        expansions=["referenced_tweets.id", "author_id"],
        max_results=10
    )

    if not tweets.data:
        return since_id

    for tweet in reversed(tweets.data):
        print(f"🕵️ Trigger found: {tweet.id}")
        try:
            referenced = tweet.referenced_tweets
            if not referenced or referenced[0].type != "replied_to":
                continue

            original_tweet_id = referenced[0].id
            original_tweet = client.get_tweet(original_tweet_id, expansions=["author_id"], tweet_fields=["author_id"])
            author_id = original_tweet.data.author_id

            user_response = client.get_user(
                id=author_id,
                user_fields=["created_at", "description", "public_metrics"]
            )

            report = analyze_account(client, user_response.data)
            send_reply(client, tweet, user_response.data.username, report)

        except Exception as e:
            print("❌ Error processing tweet:", e)

        since_id = max(tweet.id, since_id or tweet.id)

    return since_id
