from twitterApi import twitterApi



# Authentication Test
print(twitterApi.twitter_api.VerifyCredentials())

"""Building Test Set Function
Tweets are downloaded  for the search term 
"""


def buildTestSet(search_keyword):
    try:
        tweets_fetched = twitterApi.twitter_api.GetSearch(search_keyword, count=100)

        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)

        for status in tweets_fetched:
            # return {"text": status.text, "label": None}
            print({"text":status.text})

    except:
        print("Unfortunately, something went wrong..")
        return None


# Testing our Function
"""Showing four among all downloaded tweets"""

search_term = input("Enter a search keyword: ")
testDataSet = buildTestSet(search_term)

print(testDataSet)

