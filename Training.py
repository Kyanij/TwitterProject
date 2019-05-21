from TwitterApi.twitterApi import twitter_api

# Building Training Set


def build_training_set(corpus_file, tweet_data_file):
    import csv
    import time

    corpus = []  # creating list of corpus

    with open(corpus_file, "r") as csvfile:
        lineReader = csv.reader(csvfile, delimiter=',')  # separating each term by comma
        for row in lineReader:
            corpus.append({"tweet_id": row[2], "label": row[1], "topic": row[0]})  # appending in corpus list

    # To download 5000 tweets
    rate_limit = 180
    sleep_time = 900/180

    trainingDataSet = []  # empty list created to store training data set

    for tweet in corpus:
        try:
            status = twitter_api.GetStatus(tweet["tweet_id"])  # status from the id are stored in status
            print("Tweet fetched\t" + status.text)  # text from status are printed out
            tweet["text"] = status.text  # stored the text in tweet text
            trainingDataSet.append(tweet)  # All tweet are append in trainingDataSet list
            time.sleep(sleep_time)

        except:
            continue

    # print(trainingDataSet)

# writing trainingDataSet in the empty Csv file

    with open(tweet_data_file, "w") as csvfile:
        linewriter = csv.writer(csvfile, delimiter=',')
        for tweet in trainingDataSet:
            try:
                linewriter.writerow([tweet["tweet_id"], tweet["text"], tweet["label"], tweet["topic"]])
            except Exception as e:
                print(e)
    return trainingDataSet


corpus_file = "corpus.csv"
tweet_data_file = "TrainData.csv"
trainingData = build_training_set(corpus_file, tweet_data_file)
print(trainingData)




