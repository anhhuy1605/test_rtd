"""
Utilities for authentication & authorization
"""
from __future__ import absolute_import

import logging

import tweepy
from tweepy.error import TweepError, RateLimitError

from responsebot.common.exceptions import AuthenticationError, APIQuotaError
from responsebot.responsebot_client import ResponseBotClient


def auth(consumer_key, consumer_secret, token_key, token_secret):
    """
    Perform authentication with Twitter and return a client instance to communicate with Twitter

    :param str consumer_key: Consumer key provided by Twitter
    :param str consumer_secret: Consumer secret provided by Twitter
    :param str token_key: App token key provided by Twitter
    :param str token_secret: App token secret provided by Twitter
    :return: client instance to execute twitter action
    :rtype: :class:`~responsebot.responsebot_client.ResponseBotClient`
    :raises: :class:`~responsebot.common.exceptions.AuthenticationError`: If failed to authenticate
    :raises: :class:`~responsebot.common.exceptions.APIQuotaError`: If API call rate reached limit
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token_key, token_secret)

    api = tweepy.API(auth)
    try:
        api.verify_credentials()
    except RateLimitError as e:
        raise APIQuotaError(e.args[0][0]['message'])
    except TweepError as e:
        raise AuthenticationError(e.args[0][0]['message'])
    else:
        logging.info('Successfully authenticated as %s' % api.me().screen_name)

        return ResponseBotClient(client=api)
