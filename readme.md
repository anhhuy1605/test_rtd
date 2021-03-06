# ResponseBot
[![Circle CI](https://circleci.com/gh/EastAgile/twitterbot.svg?style=svg)](https://circleci.com/gh/EastAgile/twitterbot)
[![Coverage Status](https://coveralls.io/repos/github/EastAgile/twitterbot/badge.svg?branch=master)](https://coveralls.io/github/EastAgile/twitterbot?branch=master)

## Description
A framework for developing listen-and-answer twitter bots.

## Installation
```
pip install responsebot
```

## Examples
### Basic usage
* Create a class to handle incoming tweet

```
from responsebot.handlers.base import BaseTweetHandler


class MyTweetHandler(BaseTweetHandler):
    def on_tweet(self, tweet):
        print('Received tweet: %s from %s' % (tweet.text, tweet.user.screen_name))
```

* Create a `.responsebot` file in your project root with your Twitter API credentials (which can be obtained after you created a Twitter application [here](https://apps.twitter.com/))

```
[auth]
consumer_key = <consumer_key>
consumer_secret = <consumer_secret>
token_key = <token_key>
token_secret = <token_secret>
```

* Run in your project root

```
$ start_responsebot --handlers-package <python path to your package/module>
```

* Or use responsebot as a library

```
from responsebot.responsebot import ResponseBot


ResponseBot(handlers_package='<python path to your package/module>').start()
```

## [Documentation](https://responsebot.readthedocs.org)
