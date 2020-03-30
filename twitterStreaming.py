import tweepy
import json
import re

class HalifaxStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        tweetsData = {}
        with open('fetchedTweets.json','r') as tweets:
           tweetsData = json.load(tweets)  #preserve tweets in json file
        with open('fetchedTweets.json','w') as tweets:
           print("-----------------Total saved tweets in json: "+str(len(tweetsData["tweets"]))+" ------------------")
           tweetText = status.text
           print("Original Tweet:  "+tweetText)
           tweetText = re.sub(r"http\S+","",tweetText)  #remove URL from tweet
           print("Tweet After URL removed: "+tweetText)
           tweetText = re.sub(r'[^\w\s,]','',tweetText) #remove emoticons from tweet
           print("Tweet After Emojis Removed: "+tweetText)
           tweetLocation=""
           if status.place!=None:
               tweetLocation=status.place.full_name
           tweetsData["tweets"].append({"Tweet":status.text,"DateTime":status.created_at.strftime("%d-%b-%Y %H:%M:%S"),"Author":status.author.screen_name,"Location":tweetLocation})
           json.dump(tweetsData, tweets)
    def on_error(self, status_code):
        if status_code == 420:
             return False


cKey = "2STNH5Zi4bScoOlhusasBrXX3"
cSecret = "mzsjjpgDDINb7DWJgjEPhDaRAQa4AKzdWiz6RYph6p5sKx83Ee"
aToken = "3295799016-gsW8SahtAMO7abhLEZYsiIXGh80GYF9SUf960a2"
aSecret = "Vg07dtSoLIwhOYs4QSdN9yBx75GCIYeJ88k3HdOdGizRy"


auth = tweepy.OAuthHandler(cKey, cSecret)
auth.set_access_token(aToken,aSecret)


halifaxStreamListener = HalifaxStreamListener()
streamHalifax = tweepy.Stream(auth, listener=halifaxStreamListener)
streamHalifax.filter(track=['Halifax'])

