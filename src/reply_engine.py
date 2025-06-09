def send_reply(client, trigger_tweet, username, report):
    trust_score = "✅ Looks pretty trustworthy!" if report["trusted_count"] >= 2 else "⚠️ Might be worth a second look."

    reply_text = (
        f"Checking out @{username} 👀\n\n"
        f"• Around for {report['age_years']} years\n"
        f"• Follower ratio: {report['ratio']}\n"
        f"• Bio says: “{report['bio'][:50]}...”\n"
        f"• Avg likes: {report['avg_likes']} ❤️ / Retweets: {report['avg_rts']} 🔁\n"
        f"• General vibe: {report['sentiment']}\n"
        f"• Followed by {report['trusted_count']} trusted folks\n\n"
        f"{trust_score}"
    )

    try:
        client.create_tweet(
            text=f"@{trigger_tweet.author_id} {reply_text}",
            in_reply_to_tweet_id=trigger_tweet.id
        )
        print("✅ Replied with trust report")
    except Exception as e:
        print("❌ Failed to reply:", e)
