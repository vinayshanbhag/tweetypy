#!/usr/bin/env python3
""" tweety.py: Use tweepy to post tweets 
    Vinay Shanbhag 2016
"""
import tweepy, keyring

def main():
    """ Create an app at https://apps.twitter.com/
        Under Keys and Access Tokens tab, find and save the following in keyring:
          Consumer Key (API Key)
          Consumer Secret (API Secret)
          Access Token
          Access Token Secret
    """
    auth = tweepy.OAuthHandler(
        keyring.get_password('twitterkeys','consumer_key'),
        keyring.get_password('twitterkeys','consumer_secret'))
    auth.set_access_token(
        keyring.get_password('twitterkeys','access_token'),
        keyring.get_password('twitterkeys','access_token_secret'))
    
    api = tweepy.API(auth)
    
    #
    # Do something here to generate message to tweet
    #
    
    status = api.update_status(status=your_message)
    
if __name__ == "__main__":
    main()
