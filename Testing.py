from twitterApi import twitterApi


# test authentication

# print(twitterApi.twitter_api.VerifyCredentials())

"""Building Test Set Function
Tweets are downloaded  for the search term 
"""


def buildTestSet(search_keyword):
    try:
        listofTweet = []
        tweets_fetched = twitterApi.twitter_api.GetSearch(search_keyword, count=100)

        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)

        for status in tweets_fetched:
            testdata = open("TestData.csv", "a")
            testdata.write(status.text)
            listofTweet.append({"text": status.text, "label": None})
        return listofTweet

        # if (testdata):
        #     print("Successfully file created")

    except:
        print("Unfortunately, something went wrong..")
        return None


# Testing our Function




