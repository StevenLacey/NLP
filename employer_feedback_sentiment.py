# Gets the average sentiment of employer comments for a population of students. Can run this for multiple populations and compare sentiment
# of employer comments for different populations of students. 

# Import libraries
import tweepy
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import preprocessor as p
import statistics
from typing import List
import pandas as pd
import nltk

# Import data from Excel file
math_1201 = pd.read_excel("C:\\Users\\s4lacey\\PycharmProjects\\pythonProject23\\Math_1201.xlsx")
math_1201_list = math_1201['COMMENTS_SUPERVISOR'].to_list()

# Clean up data to only include instances of string comments and put in a list. 
math_1201_string_list = []
for i in range(0, len(math_1201_list)):
    if isinstance(math_1201_list[i], str):
        math_1201_string_list.append(math_1201_list[i])

# Clean the comments further. 
def clean_comments(math_1201_string_list: List[str]) -> List[str]:
    cleaned_comments = []
    for comment in math_1201_string_list:
        cleaned_comments.append(p.clean(comment))
    return cleaned_comments
Cleaned_math_1201 = clean_comments(math_1201_string_list)

#Get the sentiment of each comment and put in a list. 
def get_sentiment(all_tweets: List[str]) -> List[float]:
    sentiment_scores = []
    sentiment_subjectivity = []
    for tweet in all_tweets:
        blob = TextBlob(tweet)
        sentiment_scores.append(blob.sentiment.polarity)
    return sentiment_scores
math_1201_sentiment_scores = get_sentiment(Cleaned_math_1201)


# Get the average sentiment for the population of students. 
average_score = statistics.mean(math_1201_sentiment_scores)

# Create a dataframe of the comments and sentiments, then return it to a dataframe. 
comments_and_sentiment = pd.DataFrame({'Comments' : math_1201_string_list, 'Sentiment' : math_1201_sentiment_scores})
comments_and_sentiment.to_csv("comments_and_sentiment.csv")
