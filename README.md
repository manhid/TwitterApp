## Personal Information
	Manuel Hidalgo

	www.linkedin.com/in/manhid
	manuelehidalgom@gmail.com
	+1 (585) 360-9437

## Twitter App
	I chose to develop the Twitter app because I was curious about working with social media APIs, extracting data and displaying/analyzing the results.

	The application is implemented in Python using the Flask framework for web development and the Tweepy library to connect with the Twitter API. The backend language and framework were selected because I wanted to take the opportunity to learn web app development in Python since most of my experience is with C# and .NET.

### Required OS and libraries
	OS: The application was developed using Windows 10

	Software/Libraries required:
		● Python 3.6.0
		● flask         ( pip install flask )
		● flask-wtf  ( pip install flask-wtf )
		● tweepy    ( pip install tweepy  )
		● pandas    ( pip install pandas  )
		● numpy    ( pip install numpy  )

### How to use/test provided application
	To run the application, install Python and the required libraries in the above section. Then run the command ‘python run.py’ to run the application and open localhost in the browser.

	The home page provides a view to fill in the criteria to filter tweets. Possible criteria::
		1.	Number of tweets: (Required) The number of tweets to get from the query. Must be a number between [1-200]. An error message will be displayed if the input is missing or if the number is out of bounds.
		2.	Twitter username(s): (Optional) A list of comma separated (,) usernames. For example: ‘username_1,username_2’. If username(s) are specified, no search term, or location string can be specified. An error message will be displayed if the format is incorrect or if any user in the list is not a valid Twitter user.
		3.	Search term: (Optional) Search term criteria to filter the tweets. If a search term is specified, no Twitter username(s) can be specified
		4.	Location string: A location string of the format latitude,longitude,radius. For example: for Bolton, CT: ‘41.7797494,-72.4183382,50km’. It accepts radius in ‘km’ and ‘mi’. If a Location string is specified, no Twitter username(s) can be specified. An error message will be displayed if the format is incorrect or if latitude, longitude or radius is incorrect.
		5.	Locate me: Fills in the location string with the current location

		* At list one of three criteria: Twitter username(s), Search term or Location string must be filled in to get tweets


