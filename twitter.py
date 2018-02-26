## import the libraries
import tweepy, codecs

## fill in your Twitter credentials 
consumer_key = 'fzpCPYDGy4w5dNbOflgLmHDtb'
consumer_secret = '4lyP3E8Z2GnKn7SiijztFMlWpLnEkGmEXiad7pEYUCFDcwPUfv'
access_token = '727279051170181121DLwIHFIoJlMfDPVoH62NJ6NXcDBrlL1'
access_token_secret = 'MiPhv7luIqWLYrUktTvODPfvqo6bbJZkxEXUtUtJCkIVH'

## let Tweepy set up an instance of the REST API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

## fill in your search query and store your results in a variable
results = api.search(q = "your search term here", lang = "en", result_type = "recent", count = 1000)

## use the codecs library to write the text of the Tweets to a .txt file
file = codecs.open("twitterresults.txt", "w", "utf-8")
for result in results:
	file.write(result.text)
	file.write("\n")
file.close()