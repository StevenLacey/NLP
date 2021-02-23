# Makes a program to get the sentiment of two keywords for recent tweets on twitter then compares them and returns which keyword has higher sentiment. 

#Import Libraries
import tweepy
from textblob import TextBlob
import preprocessor as p
import statistics
from typing import List

#Connect to Twitter API. Put your key's into the consumer_key and consumer_secret variables
consumer_key = ""
consumer_secret = ""
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

#Get all the tweets for a keyword
def get_tweets(keyword: str) -> List[str]:
    all_tweets = []
    for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode='extended', lang='en').items(100):
        all_tweets.append(tweet.full_text)
    return all_tweets

#Clean up the tweets data
def clean_tweets(all_tweets: List[str]) -> List[str]:
    tweets_clean = []
    for tweet in all_tweets:
        tweets_clean.append(p.clean(tweet))
    return tweets_clean

#Get the sentiment for each tweer
def get_sentiment(all_tweets: List[str]) -> List[float]:
    sentiment_scores = []
    for tweet in all_tweets:
        blob = TextBlob(tweet)
        sentiment_scores.append(blob.sentiment.polarity)
    return sentiment_scores

# Get the average sentiment for keyword
def generate_average_sentiment_score( keyword: str) -> int:
    tweets = get_tweets(keyword)
    tweets_clean = clean_tweets(tweets)
    print(tweets_clean)
    sentiment_scores = get_sentiment(tweets_clean)
    print(sentiment_scores)
    average_score = statistics.mean(sentiment_scores)
    return average_score

# Create the program to access via terminal to input desired keywords and generate results of which keyword has higher sentiment from the twitter population for last n tweets
if __name__ == "__main__":
    print("What does the world prefer?")
    first_thing = input()
    print("...or...")
    second_thing = input()
    print("\n")

    first_score = generate_average_sentiment_score(first_thing)
    second_score = generate_average_sentiment_score(second_thing)

    if first_score > second_score:
        print(f"Humanity prefers {first_thing} over {second_thing}")
        print(first_score, second_score)

    else:
        print(f"Humanity prefers {second_thing} over {first_thing}")
        print(first_score, second_score)
