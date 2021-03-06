from unittest.case import TestCase

from tweepy.error import TweepError

from responsebot.common.constants import TWITTER_TWEET_NOT_FOUND_ERROR, TWITTER_USER_NOT_FOUND_ERROR, \
    TWITTER_PAGE_DOES_NOT_EXISTS_ERROR, TWITTER_DELETE_OTHER_USER_TWEET
from responsebot.common.exceptions import APIError
from responsebot.responsebot_client import ResponseBotClient

try:
    from mock import MagicMock
except ImportError:
    from unittest.mock import MagicMock


class TweetClientTestCase(TestCase):
    def setUp(self):
        self.real_client = MagicMock()
        self.client = ResponseBotClient(self.real_client)

    def test_post_new_tweet(self):
        self.real_client.update_status = MagicMock(return_value=MagicMock(_json={
            'some_key': 'some value',
        }))

        tweet = self.client.tweet('some text')

        self.real_client.update_status.assert_called_once_with('some text')
        self.assertEqual(tweet.some_key, 'some value')

    def test_get_tweet(self):
        self.real_client.get_status = MagicMock(return_value=MagicMock(_json={
            'some_key': 'some value',
        }))

        tweet = self.client.get_tweet(123)

        self.real_client.get_status.assert_called_once_with(123)
        self.assertEqual(tweet.some_key, 'some value')

    def test_get_non_existent_tweet(self):
        exception = TweepError(reason='some reason', api_code=TWITTER_TWEET_NOT_FOUND_ERROR)
        self.real_client.get_status = MagicMock(
            side_effect=exception
        )

        tweet = self.client.get_tweet(123)

        self.real_client.get_status.assert_called_once_with(123)
        self.assertIsNone(tweet)

    def test_get_tweet_encounter_error(self):
        self.real_client.get_status = MagicMock(
            side_effect=TweepError(reason='some reason')
        )

        self.assertRaises(APIError, self.client.get_tweet, 123)

    def test_get_user(self):
        self.real_client.get_user = MagicMock(return_value=MagicMock(_json={
            'some_key': 'some value',
        }))

        user = self.client.get_user(123)

        self.real_client.get_user.assert_called_once_with(123)
        self.assertEqual(user.some_key, 'some value')

    def test_get_non_existent_user(self):
        exception = TweepError(reason='some reason', api_code=TWITTER_USER_NOT_FOUND_ERROR)
        self.real_client.get_user = MagicMock(
            side_effect=exception
        )

        user = self.client.get_user(123)

        self.real_client.get_user.assert_called_once_with(123)
        self.assertIsNone(user)

    def test_get_user_encounter_error(self):
        self.real_client.get_user = MagicMock(
            side_effect=TweepError(reason='some reason')
        )

        self.assertRaises(APIError, self.client.get_user, 123)

    def test_remove_tweet(self):
        self.real_client.destroy_status = MagicMock()

        result = self.client.remove_tweet(123)

        self.real_client.destroy_status.assert_called_once_with(123)
        self.assertTrue(result)

    def test_remove_non_existent_tweet(self):
        exception = TweepError(reason='some reason', api_code=TWITTER_PAGE_DOES_NOT_EXISTS_ERROR)
        self.real_client.destroy_status = MagicMock(
            side_effect=exception
        )

        result = self.client.remove_tweet(123)

        self.real_client.destroy_status.assert_called_once_with(123)
        self.assertFalse(result)

    def test_remove_others_tweet(self):
        exception = TweepError(reason='some reason', api_code=TWITTER_DELETE_OTHER_USER_TWEET)
        self.real_client.destroy_status = MagicMock(
            side_effect=exception
        )

        result = self.client.remove_tweet(123)

        self.real_client.destroy_status.assert_called_once_with(123)
        self.assertFalse(result)

    def test_remove_tweet_encounter_error(self):
        self.real_client.destroy_status = MagicMock(
            side_effect=TweepError(reason='some reason')
        )

        self.assertRaises(APIError, self.client.remove_tweet, 123)

    def test_retweet(self):
        self.real_client.retweet = MagicMock()

        result = self.client.retweet(123)

        self.real_client.retweet.assert_called_once_with(123)
        self.assertTrue(result)

    def test_retweet_non_existent_tweet(self):
        exception = TweepError(reason='some reason', api_code=TWITTER_PAGE_DOES_NOT_EXISTS_ERROR)
        self.real_client.retweet = MagicMock(side_effect=exception)

        result = self.client.retweet(123)

        self.real_client.retweet.assert_called_once_with(123)
        self.assertFalse(result)

    def test_retweet_encounter_error(self):
        self.real_client.retweet = MagicMock(
            side_effect=TweepError(reason='some reason')
        )

        self.assertRaises(APIError, self.client.retweet, 123)
