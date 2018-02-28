# import the libraries
import tweepy
import codecs

# fill in your Twitter credentials
consumer_key = 'kwrWHXJppr4uaDJb1yBBUe3Sy'
consumer_secret = '1o1BvBTvBxvcyPqBdG6q1d8irBfl955IVnjPwn7ja0uYNaTvLA'
access_token = '727279051170181121DVAUULh0SeCESGuDbuJn9rq4pvdXTGQ'
access_token_secret = 'jeW3OS3Lg5YrQGKqJcuwX6vDHkFTbEL1mzbkdhbhIjqf2'

# let Tweepy set up an instance of the REST API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# fill in your search query and store your results in a variable
results = api.search(q = "your search term here", lang = "en", result_type = "recent", count = 1000)

# use the codecs library to write the text of the Tweets to a .txt file
file = codecs.open("twitterresults.txt", "w", "utf-8")
for result in results:
	file.write(result.text)
	file.write("\n")
file.close()
