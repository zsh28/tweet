
# 🛡️ RUGGUARD – Solana Trustworthiness Bot for X (Twitter)

## ✨ Features

- 🧠 Listens for `"riddle me this"` replies
- 👤 Analyzes the **original tweet's author**
- 📊 Evaluates:
  - Account age
  - Follower/following ratio
  - Bio content (length, suspicious keywords)
  - Engagement metrics (likes, retweets)
  - Sentiment from recent tweets
  - Trusted followers cross-check
- 🤖 Posts a detailed trust report **as a reply**
- ☁️ Deployable on Replit or any Python 3.12+ environment

## 📂 Project Structure

```

rugguard/
├── main.py                  # Entry point: runs the bot loop
├── .env                     # API credentials (not committed)
├── requirements.txt         # Dependencies
├── config/
│   └── x_api.py       # Auth & Tweepy v2 Client setup
└── src/
├── analyzer.py          # Analyzes a user's trust profile
├── listener.py          # Detects trigger tweets
├── reply_engine.py      # Generates & posts reply
└── trusted_accounts.py  # Fetches & caches trusted user IDs

````

 

## ⚙️ Setup & Installation

### 1. Clone the Repo

```bash
git clone https://github.com/zsh28/rugguard.git
cd rugguard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

### 2. Create `.env`

In the root directory, create a `.env` file:

```env
X_API_KEY=your_api_key
X_API_SECRET=your_api_secret
X_ACCESS_TOKEN=your_access_token
X_ACCESS_SECRET=your_access_secret
X_BEARER_TOKEN=your_bearer_token
```

You can obtain these credentials from your [X Developer Portal](https://developer.x.com/en/portal).

**Tip:** On Replit, use the "Secrets" tab to add these instead.

 

## ▶️ Run the Bot

```bash
python main.py
```

This will start the bot in polling mode (checks every 3 minutes by default). It will detect trigger phrases and respond appropriately.

 

## 🧪 How It Works

1. The bot runs and listens for replies like:
   `@<botname> riddle me this`
2. It checks which tweet this was replying to.
3. It fetches and analyzes the **author** of that original tweet.
4. It evaluates the account based on:
   * Age (in years)
   * Engagement (likes, retweets)
   * Follower/following ratio
   * Sentiment of recent tweets
   * Keywords in bio
   * Whether they are followed by **trusted accounts**
5. It posts a **reply to the "riddle me this" tweet**, summarizing the findings.

## 📈 Example Trust Report

```
@user 🧠 Trust Report for @target
• Age: 2.6 yrs
• F/F Ratio: 2.4
• Bio: “Solana dev, DAO governor...”
• Engagement: 21❤️ / 7🔁
• Sentiment: 0.18
• Followed by 3 trusted accounts
Verdict: ✅ Reliable
```
