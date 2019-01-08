from flask import render_template, url_for, flash, redirect, request
from KonicaTwitter import app
from KonicaTwitter.forms import UserInputForm
from KonicaTwitter.tweepy_api import TwitterFetcher

import pandas as pd

tweets_list = []

tweets_filter = {
    'num_tweets': '',
    'twitter_username': '',
    'search_term': '',
    'location_string': '',
}


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = UserInputForm()

    if form.validate_on_submit():
        global tweets_filter
        global tweets_list

        tweets_list = []

        twitter_username = []
        search_term = form.search_term.data
        num_tweets = form.num_tweets.data
        locate_me = form.locate_me.data
        location_string = form.location_string.data

        t_users = (form.twitter_username.data).split(',')
        for t_user in t_users:
            twitter_username.append(t_user.strip())

        print("test" + form.location_string.data)

        # Get location_string unless locate_me is active
        tweets_filter = {
            'num_tweets': form.num_tweets.data,
            'twitter_username': form.twitter_username.data,
            'search_term': form.search_term.data,
            'location_string': form.location_string.data,
        }

        # Get tweets based on criteria
        twitter_fetcher = TwitterFetcher(twitter_username, num_tweets, search_term, location_string)

        if len(twitter_username) > 1 or (len(twitter_username) == 1 and twitter_username[0].strip() != ''):
            df = twitter_fetcher.get_user_timeline()
        else:
            df = twitter_fetcher.search_tweets()

        indx = 0
        for index, row in df.iterrows():
            tweet = {
                'tweet': row['tweets'],
                'id': row['id'],
                'len': row['len'],
                'date': row['date'],
                'source': row['source'],
                'likes': row['likes'],
                'indx': str(indx)
            }
            indx += 1
            tweets_list.append(tweet)

        return redirect(url_for('tweets'))
    return render_template('home.html', form=form)


@app.route("/tweets", methods=['GET', 'POST'])
def tweets():
    return render_template('tweets.html', tweets_list=tweets_list, tweets_filter=tweets_filter)
