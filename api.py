import praw
from keys import getID, getSecret, getAgent

reddit = praw.Reddit(client_id= getID,
                     client_secret=getSecret,
                     user_agent=getAgent)
