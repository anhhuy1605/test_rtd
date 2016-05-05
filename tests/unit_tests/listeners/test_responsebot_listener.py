from unittest.case import TestCase

from responsebot.common.exceptions import UserHandlerException
from responsebot.listeners.responsebot_listener import ResponseBotListener

try:
    from mock import MagicMock
except ImportError:
    from unittest.mock import MagicMock


class ResponseBotListenerTestCase(TestCase):
    def test_register_handlers(self):
        handler_class_1 = MagicMock(return_value='handler 1')
        handler_class_2 = MagicMock(return_value='handler 2')

        listener = ResponseBotListener(handler_classes=[handler_class_1, handler_class_2], client=None)

        self.assertEqual(listener.handlers, ['handler 1', 'handler 2'])

    def test_call_handlers_on_tweet(self):
        handler_1 = MagicMock(on_tweet=MagicMock())
        handler_2 = MagicMock(on_tweet=MagicMock())
        listener = ResponseBotListener(handler_classes=[], client=None)
        listener.handlers = [handler_1, handler_2]

        tweet = MagicMock(text='tweet')
        listener.on_tweet(tweet)

        handler_1.on_tweet.assert_called_once_with(tweet)
        handler_2.on_tweet.assert_called_once_with(tweet)

    def test_raise_user_handler_exception(self):
        handler_class = MagicMock(side_effect=Exception('some error'))

        self.assertRaises(UserHandlerException, ResponseBotListener, handler_classes=[handler_class], client=None)

    def test_raise_user_handler_exception_on_tweet(self):
        handler_class = MagicMock(on_tweet=MagicMock())
        handler_class().on_tweet = MagicMock(side_effect=Exception('some error unknown'))
        tweet = MagicMock(text='tweet')

        listener = ResponseBotListener(handler_classes=[handler_class], client=None)

        self.assertRaises(UserHandlerException, listener.on_tweet, tweet=tweet)
