"""
Exceptions and errors used by Tweet Bot
"""
class NotFreeToTweetError(Exception):
    """
    Error to indicate Tweeter fails to post some status due to Twitter API's status update rate limit
    """
    pass


class MissingConfigException(Exception):
    """
    Exception to indicate a required configuration for Tweet Bot is not found from config file or CLI
    """
    pass


class AuthenticationError(Exception):
    """
    Error to indicate Tweet Bot failed to authenticate with the provided credentials
    """
    pass


class APIError(Exception):
    """Generic API error"""
    pass


class APIQuotaError(APIError):
    """
    Error to indicate some API limit was reached
    """
    pass


class UnknownAPIError(APIError):
    """
    Unknown error from executing API
    """
    pass


class UserHandlerException(Exception):
    """
    Error to indicate some error caused by a user's handler
    """
    pass
