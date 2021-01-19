import tweepy
import configparser
from typing import Tuple


def get_authentication_keys(config_file_path: str) -> Tuple[str, str, str, str]:
    """Return the necessary authentication keys to access Twitter API."""
    config = configparser.ConfigParser()
    config.read(config_file_path)
    consumer_key = config["Twitter"]["consumer_key"]
    consumer_secret = config["Twitter"]["consumer_secret"]
    access_token = config["Twitter"]["access_token"]
    access_token_secret = config["Twitter"]["access_token_secret"]
    return consumer_key, consumer_secret, access_token, access_token_secret


def get_twitter_api(config_file_path: str = 'twitter_oauth.ini'):
    """Return the twitter API after performing authenticatiion with a config file"""
    consumer_key, consumer_secret, access_token, access_token_secret = get_authentication_keys(config_file_path)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api
