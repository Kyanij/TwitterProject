from nltk.tokenize import word_tokenize

from PreProcessingTest import PreProcessing
import csv
import re


class PreProcessTrain(PreProcessing):
    def __int__(self):
        super().__init__()

    def process_tweets(self, list_of_tweets):
        processed_tweets = []
        for tweet in list_of_tweets:
            # print(tweet)
            processed_tweets.append((self.process_tweet(tweet[1])))
        return processed_tweets

    def process_tweet(self, tweet):
        tweet = tweet.lower()  # lower case
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)  # remove URLS
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet)  # remove usernames
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)  # remove the # in hashtag
        tweet = word_tokenize(tweet)  # remove repeated characters (helloooooo into hello)
        for word in tweet:
            if word not in self.stopwords:
                return word


tweetProcessor = PreProcessTrain()



with open('TrainData.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    trainList = []
    for row in csv_reader:
        trainList.append(row)
#
preprocessTrainingSet = tweetProcessor.process_tweets(trainList)
print(preprocessTrainingSet)  # checking










