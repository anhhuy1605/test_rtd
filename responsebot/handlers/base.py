class BaseTweetHandler(object):
    """
    An abstract base tweet handler class for the users to subclass.
    """

    def __init__(self, client=None):
        """

        :param client: Some Twitter API client for authentication. E.g. :class:`~responsebot.tweet_client.TweetClient`
        """
        self.client = client

    def on_tweet(self, tweet):
        """
        Callback for when a tweet appears in user timeline

        :param tweet: The incoming tweet
        :type tweet: :class:`~responsebot.models.Tweet`
        """
        raise NotImplementedError
