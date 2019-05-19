from twitterApi import twitterApi

# Authentication Test
print(twitterApi.twitter_api.VerifyCredentials())



#Building TrainingSet Function

def buildTrainingSet(corpusFile, tweetDataFile):
    import csv

    corpus = []

    with open("corpus.csv", 'r') as csvfile:
        lineReader = csv.reader(csvfile, delimiter=',')
        print(lineReader)
        for row in lineReader:
            corpus.append({"tweet_id":row[2], "label":row[1], "topic":row[0]})

    rate_limit = 100
    sleep_time = 900/180

    trainingDataSet = []

    for tweet in corpus:
        try:
            status = twitterApi.twitter_api.GetStatus(tweet["tweet_id"])
            print("Tweet fetched" + status)
            trainingDataSet.append(tweet)
            time.sleep(sleep_time)

        except:
            continue

    with open("train.csv", "w") as csvfile:
        linewriter = csv.writer(csvfile, delimiter=',')
        for tweet in trainingDataSet:
            try:
                linewriter.writerow([tweet["tweet_id"], tweet["text"], tweet["label"], tweet["topic"]])
            except Exception as e:
                print(e)
    return trainingDataSet

# Testing TrainingSet function
buildTrainingSet("corpus.csv", "train.csv")



# Testing our Function
"""Showing four among all downloaded tweets"""

search_term = input("Enter a search keyword: ")
testDataSet = buildTestSet(search_term)
#
# print(testDataSet)



