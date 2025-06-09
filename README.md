# 🛡️ RUGGUARD – Solana Trustworthiness Bot for X (Twitter)

## ✨ Features

* 🧠 Listens for replies containing `"riddle me this"`
* 👤 Analyzes the **author of the original tweet**
* 📊 Evaluates:

  * Account age
  * Follower/following ratio
  * Bio content (length, suspicious keywords)
  * Engagement metrics (likes, retweets)
  * Sentiment from recent tweets
  * Whether they’re followed by trusted accounts
* 💬 Posts a **natural-sounding trust report** as a reply
* ☁️ Easy deployment on Replit or any Python 3.12+ environment

## 📂 Project Structure

```
rugguard/
├── main.py                  # Entry point: runs the bot loop
├── .env                     # API credentials (not committed)
├── requirements.txt         # Dependencies
├── config/
│   └── x_api.py             # Auth & Tweepy v2 client setup
└── src/
    ├── analyzer.py          # Analyzes a user's trust profile
    ├── listener.py          # Detects trigger tweets
    ├── reply_engine.py      # Generates & posts natural reply
    └── trusted_accounts.py  # Hardcoded trusted account handles
```

## ⚙️ Setup & Installation

### 1. Clone the Repo

```bash
git clone https://github.com/zsh28/tweet.git
cd rugguard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Create `.env`

In the root directory, create a `.env` file:

```env
X_API_KEY=your_api_key
X_API_SECRET=your_api_secret
X_ACCESS_TOKEN=your_access_token
X_ACCESS_SECRET=your_access_secret
X_BEARER_TOKEN=your_bearer_token
```

You can find these credentials in your [X Developer Portal](https://developer.x.com/en/portal).

> 💡 **Tip**: On Replit, use the **Secrets** tab instead of a `.env` file.

## ▶️ Run the Bot

```bash
python main.py
```

This starts the bot in polling mode (checking for new replies every \~3 minutes). When someone tweets `"riddle me this"` in reply, the bot analyzes the original tweet's author and responds.

## 🧪 How It Works

1. The bot watches for replies like:
   `@<bot_username> riddle me this`
2. It checks the original tweet being replied to.
3. It analyzes that tweet's author based on:

   * How long the account's been around
   * Follower/following ratio
   * Sentiment of recent tweets
   * Bio quality and keyword flags
   * Engagement (likes and RTs)
   * Whether they're followed by trusted accounts
4. It replies with a **natural, helpful trust summary**.

## 📈 Example Trust Report

```
@user Checking out @target 👀

• Around for 2.6 years  
• Follower ratio: 2.4  
• Bio says: “Solana dev, DAO governor...”  
• Avg likes: 21 ❤️ / Retweets: 7 🔁  
• General vibe: 0.18  
• Followed by 3 trusted folks  

✅ Looks pretty trustworthy!
```

## 🚀 Deployment (Replit)

You can deploy RUGGUARD in minutes using Replit:

### 🛠️ 1. Create a New Repl

* Go to [https://replit.com](https://replit.com)
* Click **"+ Create Repl"**
* Choose:

  * **Language**: Python
  * **Project name**: `rugguard`

### 🔄 2. Import from GitHub

* In the project window, click **"Import from GitHub"**
* Paste your repo URL:
  `https://github.com/zsh28/tweet`
* Click **"Import"**, then **"Confirm and close"**

### 🔐 3. Set Environment Secrets

Click the **🔐 Secrets** tab and add the following keys:

| Key               | Value              |
| ----------------- | ------------------ |
| `X_API_KEY`       | Your API Key       |
| `X_API_SECRET`    | Your API Secret    |
| `X_ACCESS_TOKEN`  | Your Access Token  |
| `X_ACCESS_SECRET` | Your Access Secret |
| `X_BEARER_TOKEN`  | Your Bearer Token  |

You can get these from your [X Developer Dashboard](https://developer.x.com/en/portal/dashboard).

### ▶️ 4. Run the App

* Click the green **"Run"** button at the top
* You should see:

  ```
  🤖 RUGGUARD bot is running...
  ```

If needed, set the `.replit` run command manually:

```ini
run = "python3 main.py"
```