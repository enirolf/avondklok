import random
import schedule
import time

from config import create_api

EVENING_TWEETS = ["Naar binnen!!", "Deur dicht!", "Ja, nu!", "✔️", "Bent u binnen?!??"]
MORNING_TWEETS = [
    "U mag weer naar buiten hoor",
    "WAKKER WORDEN JE MAG NAAR BUITEN!!",
    "Hop hop naar buiten!",
]


def tweet_evening(api):
    tweet = random.choice(EVENING_TWEETS)
    api.update_status(tweet)


def tweet_morning(api):
    tweet = random.choice(MORNING_TWEETS)
    api.update_status(tweet)


def main():
    """
    Driver method
    """
    api = create_api()

    schedule.every().day.at("21:00").do(tweet_evening, api=api)
    schedule.every().day.at("04:30").do(tweet_morning, api=api)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
