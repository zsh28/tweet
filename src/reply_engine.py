def send_reply(client, trigger_tweet, username, report):
    trust_score = "✅ Reliable" if report["trusted_count"] >= 2 else "⚠️ Needs Caution"

    reply_text = (
        f"🧠 Trust Report for @{username}\n"
        f"• Age: {report['age_years']} yrs\n"
        f"• F/F Ratio: {report['ratio']}\n"
        f"• Bio: {report['bio'][:50]}...\n"
        f"• Engagement: {report['avg_likes']}❤️ / {report['avg_rts']}🔁\n"
        f"• Sentiment: {report['sentiment']}\n"
        f"• Followed by {report['trusted_count']} trusted accounts\n"
        f"Verdict: {trust_score}"
    )

    try:
        client.create_tweet(
            text=f"@{trigger_tweet.author_id} {reply_text}",
            in_reply_to_tweet_id=trigger_tweet.id
        )
        print("✅ Replied with trust report")
    except Exception as e:
        print("❌ Failed to reply:", e)
