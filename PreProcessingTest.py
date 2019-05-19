import re
import Testing
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords



class PreProcessing:
    def __init__(self):
        listUser = ('AT_USER', 'URL')
        self.stopwords = set(stopwords.words('english') + list(punctuation) + list(listUser))  # removed stopwords, punctuations and user,url
        # print(self.stopwords)

    def process_tweets(self, list_of_tweets):
        processed_tweets=[]
        for tweet in list_of_tweets:
            processed_tweets.append((self.process_tweet(tweet["text"]), tweet["label"]))
        return processed_tweets

    def process_tweet(self, tweet):

        tweet = tweet.lower()  # lower case
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)  # remove URLS
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet)  # remove usernames
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)  #remove the # in hashtag
        tweet = word_tokenize(tweet)  # remove repeated characters (helloooooo into hello)
        for word in tweet:
            if word not in self.stopwords:
                return word


# Testing process_tweets

search_term = input("Enter a search keyword: ")
testDataSet = Testing.buildTestSet(search_term)




tweetProcessor = PreProcessing()
preprocessTestSet = tweetProcessor.process_tweets(testDataSet)
print(preprocessTestSet)





# building vocabulary

# def buildVocabuary(preprocessTrainingSet):
#     all_words = []
#
#     for (words, sentiment) in preprocessTrainingSet:
#         all_words.extend(words)
#
#
#     wordlist = nltk.FreqDist(all_words)
#     word_features = wordlist.keys(
#
#     return word_features
#
#
# print(buildVocabuary(traindata))
#



