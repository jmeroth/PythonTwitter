from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


# Application Name:  wecardata


#consumer key, consumer secret, access token, access secret.
ckey="GFCnywy7AOj40e1b0E8pQSiAJ"
csecret="fxLHBuGBQy1fz59e36dJvD79BqbGvD45vGp7ripT1P4PcVX5fH"
atoken="1579574191-F7wQB8Irp2fYD3NkqJSuHI9pw0BWYhkFRc25XtM"
asecret="flmCveAtecACSqBCnxTXFvlxMbTJsCYNhBa9Lc092hqn3"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"].encode('utf-8')

        print(tweet)
        #print(all_data)

        
        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["star wars"])
