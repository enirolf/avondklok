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


def gifs(api):
    paths = ["gifs/gif1.gif", "gifs/gif2.gif", "gifs/gif3.gif"]
    return [api.media_upload(path).media_id for path in paths]


def tweet_evening(api, gif_ids):
    if random.randint(10) % 2 == 0:
        tweet = random.choice(EVENING_TWEETS)
        api.update_status(tweet)
    else:
        gif_id = random.choice(gif_ids)
        api.update_status(media_ids=[gif_id])


def tweet_morning(api):
    tweet = random.choice(MORNING_TWEETS)
    api.update_status(tweet)


def main():
    """Driver method"""

    api = create_api()
    gif_ids = gifs(api)

    schedule.every().day.at("21:00").do(tweet_evening, api=api, gif_ids=gif_ids)
    schedule.every().day.at("04:30").do(tweet_morning, api=api)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
