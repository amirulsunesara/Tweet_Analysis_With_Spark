import tweepy
import json
import re


cKey = "DJxdQEjuNruUULzZP78ZONwxY"
cSecret = "6QFApbXuK71zkNYUhAbz71zQlZ2lr1gYjm7kaNSkPhUMoSKlY9"
aToken = "3295799016-JofvqncuPVCw5FSHPq7CoiSLZnwc9CxZQrYyO9F"
aSecret = "NW67R1M3SNos8UBk5w6epLgQJj3QWq9rEELHnA4C4aBMK"


auth = tweepy.OAuthHandler(cKey, cSecret)
auth.set_access_token(aToken,aSecret)

api = tweepy.API(auth,wait_on_rate_limit=True)

searchTweets  = [model for model in tweepy.Cursor(api.search, q='Halifax').items(2000)]#get 2000 datapoints for keyword 'halifax'

tweetsData = {}
searchTweetsCount = 0
for tweetModel in searchTweets:
        searchTweetsCount+=1 #store the count of fetched tweets in current session
        print("Search tweets count:"+str(searchTweetsCount))
        with open('fetchedTweets.json','r') as tweets:
                tweetsData = json.load(tweets) #preserve data from json file and save in dictionery
        with open('fetchedTweets.json','w') as tweets:
                print("Total saved tweets in json: "+str(len(tweetsData["tweets"])))
                tweetText = tweetModel.text
                print("Original tweet:  "+tweetText)
                tweetText = re.sub(r"http\S+","",tweetText)
                print("Tweet after removing URL:  "+tweetText)
                tweetText = re.sub(r'[^\w\s,]','',tweetText)
                print("Tweet after removing Emojis: "+tweetText)
                tweetLocation=""
                if tweetModel.place!=None:
                    tweetLocation=tweetModel.place.full_name
                tweetsData["tweets"].append({"Tweet":tweetModel.text,"DateTime":tweetModel.created_at.strftime("%d-%b-%Y %H:%M%S"),"Author":tweetModel.author.screen_name,"Location":tweetLocation})
                json.dump(tweetsData, tweets)
