from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '10015791628bb0b13ma0c676dfde28ba'

from KonicaTwitter import routes
from KonicaTwitter import tweepy_api
