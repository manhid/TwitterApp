from tweepy import OAuthHandler
from tweepy import Cursor
from tweepy import API

import pandas as pd
import numpy as np

# User credentials to access Twitter API
ACCESS_TOKEN = "---"
ACCESS_TOKEN_SECRET = "---"
CONSUMER_KEY = "---"
CONSUMER_SECRET = "---"


class TwitterAutheticator():
    # Class to authenticate to twitter app

    def authenticate_twitter_api(self):
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return auth


class TwitterClient():
    # Class to manage twitter client connection to twitter API

    def __init__(self, twitter_user=None):
        self.auth = TwitterAutheticator().authenticate_twitter_api()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client


class TweetHandler():
    # Class to handle fetched tweets as data-frames from PANDAS library

    def tweets_to_dataframe(self, tweets):
        # Build dataframe of tweets
        df = pd.DataFrame(data=[tweet.full_text for tweet in tweets], columns=['tweets'])
        df['id'] = np.array([tweet.author._json['screen_name'] for tweet in tweets])
        df['len'] = np.array([len(tweet.full_text) for tweet in tweets])
        df['date'] = np.array([pd.to_datetime(tweet.created_at) for tweet in tweets])
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])

        return df


class TwitterFetcher():
    # Class to fetch tweets

    def __init__(self, users=[''], num_tweets=20, search_term='', location_string=''):
        # User input parameters
        self.users = users
        self.num_tweets = num_tweets
        self.search_term = search_term
        self.location_string = location_string

        self.tweet_handler = TweetHandler()

        # Connet to tweepy client
        self.twitter_client = TwitterClient()
        self.api = self.twitter_client.get_twitter_client_api()

    def search_tweets(self):
        # Get num_tweets that match search_term criteria and return in a dataframe
        #tweets = self.api.search(q=self.search_term + ' -filter:retweets', count=self.num_tweets, geocode=self.location_string, tweet_mode="extended")

        tweets = []
        for tweet in Cursor(self.api.search,
                            q=self.search_term + ' -filter:retweets',
                            geocode=self.location_string,
                            tweet_mode="extended").items(self.num_tweets):
            tweets.append(tweet)

        df = self.tweet_handler.tweets_to_dataframe(tweets)
        df = df.head(self.num_tweets)
        return df

    def get_user_timeline(self):
        # Dataframe to handle tweets
        df = pd.DataFrame()

        for user_id in self.users:
            # Loop over users to fetch tweets
            tweets = []
            for tweet in Cursor(self.api.user_timeline, id=user_id, tweet_mode="extended").items(self.num_tweets):
                tweets.append(tweet)

            # Save tweets to df and filter
            df2 = self.tweet_handler.tweets_to_dataframe(tweets)
            df = df.append(df2)

        # Sort by date to get the latest tweets from all users
        df = df.sort(['date'], ascending=[0])
        df = df.head(self.num_tweets)

        return df

    def is_valid_user(self, user_id):
        # determine wether the specified user is valid
        is_valid = False
        try:
            user = self.api.get_user(id=user_id)
            if not user.protected:
                is_valid = True

        except Exception:
            is_valid = False

        return is_valid
