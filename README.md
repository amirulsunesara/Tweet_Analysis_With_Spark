# Tweet Analysis with Apache Spark

Extracted data using twitter streaming and search API’s and Implemented a map reducer program in python with Apache Spark to identify essential information in tweets.

## Cloud setup process

For cloud setup we will need to signup for AWS account. After that we will need to create EC2 instance for Ubuntu Server 18.04 LTS and, later we need to set key-value for cloud access and leave rest of the configuration to default. To make a connection to cloud we will use PuTTY by entering host-name and passing private key that is generated during setup process. A screenshot of my cloud dashboard is placed in ‘screenshots’ folder.

## Data extraction process

I am using tweepy API for data extraction process. Before using this API, we need twitter developer account and generate tokens which will set into code. I have written two files for tweet extraction (twitterStreaming.py and twitterSearch.py). Tweets are streamed through twitterStreaming.py, whereas twitterSearch.py is using search API to fetch 2000 datapoints in a single go. I am limiting my search to 2000 datapoints, because I have found that twitter will black-list my account on going beyond that limit. These files are also performing cleaning process which is discussed later in this report.

## Data cleaning process

Data cleaning is also performed by same two files (twitterStreaming.py and twitterSearch.py). All URLs and emoticons are removed before saving tweet to json file, which is necessary, because some special characters might break json.

Following regular expressions are used to clean tweets.

1. Remove all http/https URLs: “http\S+”
2. Remove all emoticons (removing special characters will do this job): “[^\w\s,]”

Output after cleaning tweets will stored in fetchedTweets.json file.

## JSON Format

```JSON
{
"tweets":[{
"Tweet": "Words fail when children are taken from us too soon, especially in circumstances like this.",
"Author": "cwyyell",
"Location": "Halifax",
"DateTime": "19-Feb-2019 17:3541"
},
{
"Tweet": "This program is a great opportunity for employers to grow their businesses by employing apprentices like Cassandra ", "Author": "NSLAE",
"Location": "",
"DateTime": "19-Feb-2019 15:1958"
}]
}
```

## Store data in Mongodb

I have created a separate file(storeData.py) to store tweet data in mongodb. This file is parsing json data stored in fetchedTweets.json and storing all fields extracted including Tweet text, datetime, author and location. A screenshot showing saved data is placed in ‘screenshots’ folder.

## Data Processing (MapReduce using Apache Spark):

Pre-requisites:

1. Setup apache spark on EC2
2. Start master:
   sudo ./spark-2.4.0-bin-hadoop2.7/sbin/start-master.sh
3. Start slave:
   sudo ./spark-2.4.0-bin-hadoop2.7/sbin/start-slave.sh spark://ip-172-31-16-22.us-east-2.compute.internal:7077
   MapReduce.py file is created for finding total occurrences of string in tweets. This file takes input from fetchedTweets.json and filter out keywords mentioned in question. It uses ‘map’ and ‘reduceByKey’ function of apache spark. The output with frequency of words is stored in outputFile.txt

## Analysis

#### Which substring or word are most frequently used in your extracted tweets.

Answer: Most frequently used word is ‘immigrant’

#### Can you justify the reason by performing a new data extraction using twitter streaming API? Keep the search keyword as “Halifax”.

Answer: When I ran streaming on snow day, I find increase in use of keyword “snow storm” in tweets. There is also an increase in keyword “safe” which might be indicating the level of safety, or safe routes during snow. The keyword “immigrant” was mostly used in tweets, and even after running stream multiple times I have found an increase word count for ‘immigrant’. I believe that there are two reason for that: (1) Canada is accepting skilled immigrants all over the world. (2) An accident recently happened where immigrant children lost their life in house fire.

## Technologies used

1. Python
2. Apache Spark
3. AWS
