from config.x_api import get_client
from src.listener import process_mentions
import time
import tweepy

def main():
    print("🤖 RUGGUARD bot is running...")
    client = get_client()
    since_id = None

    while True:
        try:
            since_id = process_mentions(client, since_id)
        except tweepy.TooManyRequests as e:
            wait = int(e.response.headers.get("x-rate-limit-reset", 900))
            print(f"⚠️ Rate limit hit. Sleeping for {wait} seconds.")
            time.sleep(wait)
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            time.sleep(30)

        time.sleep(60)  # main poll interval

if __name__ == "__main__":
    main()
