import dotenv
from tweepy.api import API
from tweepy.auth import OAuthHandler
from tweepy.streaming import Stream

from responsebot.handlers.tweepy_base_handler import TweepyBaseTweetHandler
from responsebot.listeners.tweepy_wrapper_listener import TweepyListener

dotenv.load()

API_KEY = dotenv.get('API_KEY')
API_SECRET = dotenv.get('API_SECRET')
ACCESS_TOKEN = dotenv.get('ACCESS_TOKEN')
ACCESS_SECRET = dotenv.get('ACCESS_SECRET')


class PrintTweetHandler(TweepyBaseTweetHandler):
    def on_tweet(self, tweet):
        print("""
=========
User: {name}
Content:
{content}
=========
        """.format(
            name=tweet.user.screen_name,
            content=tweet.text
        ))


def authenticate():
    auth = OAuthHandler(consumer_key=API_KEY, consumer_secret=API_SECRET)
    auth.set_access_token(key=ACCESS_TOKEN, secret=ACCESS_SECRET)

    return auth


def connect_to_api(auth):
    api = API(auth_handler=auth)
    api.verify_credentials()

    return api


def run():
    # Authenticates with Twitter
    print('Auth')
    auth = authenticate()
    api = connect_to_api(auth)

    print('Handling')
    listener = TweepyListener(api)
    listener.add_handler(handler=PrintTweetHandler())

    print('Streaming')
    stream = Stream(auth=auth, listener=listener)

    stream.sample()


if __name__ == '__main__':
    run()
