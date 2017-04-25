import praw
from keys import getID, getSecret, getAgent

def main():
    #create reddit instance
    ID = getID()
    secret = getSecret()
    agent = getAgent()
    reddit = praw.Reddit(client_id= ID,
                         client_secret=secret,
                         user_agent=agent)
    #get keyword
    keyword = getKeyword()
    #get subreddit
    subreddit = getSubreddit()
    #create file necessary
    file_name = subreddit + ".txt"
    new_file = open(file_name, "w", encoding="utf8")
    #gets top 100 posts from day http://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html
    for submission in reddit.subreddit(subreddit).top('day'):
        process_submission(submission, keyword, new_file)
    new_file.close()

#also used praw documentation to help this
def process_submission(submission, keyword, new_file):
    normalized_title = submission.title.lower()
    #should get most comments from thread and add to new_file
    if keyword in normalized_title:
        #written with assistance from documentation http://praw.readthedocs.io/en/latest/tutorials/comments.html
        submission.comments.replace_more(limit=0)
        #convert to string
        for comment in submission.comments.list():
            text = str(comment.body)
            #write to file
            new_file.write(text)
            new_file.write(" ")

def getKeyword():
    #get keyword
    keyword = input('Enter topic keyword: ')
    #convert to lowercase to supplement later string comparison
    keyword = keyword.lower()
    return keyword

def getSubreddit():
    #get subreddit
    name = input('Enter subreddit name: ')
    return name
