import tweepy
from textblob import TextBlob

consumer_key='ombQw3jY2EhRdeF62smypLzdi'
consumer_secret='wLEGUEu8ba279Wr8cuZlBTZpzjIn38LSkDyo83TWRHS47dcpLA'

access_token='788674678030204928-S6AwJbskv6ffwYCbzjdP1UG1BEVHBeB'
access_token_secret='jWRAAYgqKEDPjZ3Sq4px0QYqu9qsGRTE3cVadnB41qfGU'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Alma TV')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)