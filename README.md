# Reddit PyCloud

This is our final project for CS2021 at University of Cincinnati written entirely in python. Accesses reddit API and displays comment/post data in a wordcloud format for subject analysis. Provided here is a framework. In order to use for yourself, see the **Installation** section below.

## 3rd Party Libraries Used

- PRAW
- wordcloud
- scrapy

See requirements.txt for more in-depth information.

## Installation

Clone this repository to a directory of your choosing. Then create a virtual environment in which to install/run the third-party python libraries. This project requires python 3.x to be installed on the user's machine.

```
virtualenv env1
source env1/Scripts/activate

pip install praw
pip install scrapy
pip install wordcloud
```

It is important to note that an authentic reddit account is required for accessing the reddit API. As such, log into a valid reddit account and go to your user preferences, and navigate to the apps tab. Create an app and copy your API keys to *keys.py*.
