from pymongo import MongoClient
import json

mongoClient = MongoClient('localhost',27017,username='amirul',password='amiruls',authSource='assignment2')

with open('fetchedTweets.json','r') as tweetFile:
        tweetsData = json.load(tweetFile)
        count = 0
        for tweet in tweetsData["tweets"]:
                mongoClient.assignment2.tweetCollection.insert_one(tweet)
                count += 1
        print("Inserted "+str(count)+" rows")
