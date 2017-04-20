# Reddit PyCloud

This is our final project for CS2021 at University of Cincinnati written entirely in python. Accesses reddit API and displays comment/post data in a wordcloud format for subject analysis. 

## 3rd Party Libraries Used

- PRAW
- wordcloud
- scrapy

See requirements.txt for more in-depth information.

## Installation

Clone this repository to a directory of your choosing. Then create a virtual environment in which to install/run the third-party python libraries.

```
virtualenv env1
source env1/Scripts/activate

pip install praw
pip install scrapy
pip install wordcloud
```

The program runs on its own reddit account when accessing the reddit API through PRAW. If so desired, the user can input their own API keys in api.py. 
