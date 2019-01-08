from flask_wtf import FlaskForm
from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
import re
from KonicaTwitter.tweepy_api import TwitterFetcher


class UserInputForm(FlaskForm):
    # Class form to get user input on filters to retrive tweets

    twitter_username = StringField('Twitter username(s)',
                                   validators=[Length(min=0, max=500)])
    search_term = StringField('Search term',
                              validators=[Length(min=0, max=500)])
    num_tweets = IntegerField('Number of tweets',
                              validators=[DataRequired()])
    location_string = StringField('Location string',
                                  validators=[Length(min=0, max=500)])
    locate_me = BooleanField('Get tweets around me')
    get_tweets = SubmitField('Get tweets')

    def validate_twitter_username(self, twitter_username):
        # Validate if twitter_username is a valid username

        users = (twitter_username.data).split(',')

        if len(users) > 1 or (len(users) == 1 and users[0].strip() != ''):
            twitter_fetcher = TwitterFetcher()
            for twiter_user in users:
                if not twitter_fetcher.is_valid_user(twiter_user.strip()):
                    raise ValidationError('Twitter user: ' + twiter_user.strip() + ' is not a valid user.')

    def validate_num_tweets(self, num_tweets):
        # num_tweets is a number in 1-200
        if num_tweets.data > 200 or num_tweets.data < 0:
            raise ValidationError('The number of tweets must be in [1-200]')

    def validate_location_string(self, location_string):
        # location string must match format latitud,longitud,radious(in km or mi) for example: 5.29126,52.132633,150km
        if location_string.data != '':
            location = location_string.data.split(',')

            if len(location) == 3:

                if re.match('^[0-9]+[.,]?[0-9]*$', location[0]) == None:
                    raise ValidationError('Incorrect latitude: ' + location[0]
                                          + '. Correct format is 55.5555 or -55.5555')
                if re.match('^[+-]?[0-9]+[.,]?[0-9]*$', location[1]) == None:
                    raise ValidationError('Incorrect longitude: ' + location[1] + '. Correct format is 55.5555 or -55.5555')
                if re.match('^[0-9]+(mi|Mi|mI|MI|km|KM|Km|kM)$', location[2]) == None:
                    raise ValidationError('Incorrect radius: ' + location[2] + '. Correct format is 55km or 55mi')
            else:
                raise ValidationError('Incorrect format. Correct format is "latitud,longitud,radius"')

        # At least one of the three criteria (twitter_username,serach_term,,location_string) must be specified
        if self.twitter_username.data == '' and self.search_term.data == '' and self.location_string.data == '':
            raise ValidationError('At least one of the three criteria: twitter_username, serach_term or location_string must be specified')
