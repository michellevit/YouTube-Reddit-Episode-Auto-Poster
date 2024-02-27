# YouTube-Reddit Auto Post Script 


![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![YouTube API](https://img.shields.io/badge/YouTube%20API-v3-red.svg)


A Python script which checks the Lex Fridman YouTube channel for the latest podcast episode, and posts the video to the Lex Fridman subreddit (if it has not already been posted).


## Table of Contents
- [Requirements](#requirements)
- [Resources](#resources)
- [How To Install](#how-to-install)
- [How To Run the Program](#how-to-run)
- [FAQ](#faq)
- [Troubleshooting](#troubleshooting)
- [Credits](#credits)


## Requirements<a name="requirements"></a>
- Libraries: 
  - Python 3.9
  - googleapiclient
  - mysql.connector
  - praw
  - dotenv
- Other:
 - Google account
 - YouTube API key
  - Reddit account
  - Reddit API key
  - mySQL Workbench


## Resources<a name="resources"></a>
- Google/YT API Documentation: https://github.com/googleapis/google-api-python-client
- YouTube API: https://developers.google.com/youtube/v3
- How to set-up virtual environment: https://www.youtube.com/watch?v=APOPm01BVrk&t=0s
- Python YouTube API Tutorial: https://www.youtube.com/watch?v=th5_9woFJmk
- mySQL Tutorial (setup + basic queries): https://www.youtube.com/watch?v=3vsC05rxZ8c


## How To Install<a name="how-to-install"></a>
- Install Python 3.9.13 or higher
- Create Virtual Environment (https://www.youtube.com/watch?v=APOPm01BVrk&t=0s) : 
  - Open terminal
  - cd into folder
  - create Python environment: `python -m venv project_yt_api`
  - activate the virtual environment: `project_yt_api\Scripts\activate.bat`
  - install google api: `pip install google-api-python-client`
  - install mysql.connector: `pip install mysql.connector`
  - install praw: `pip install praw`
- Install dotenv: `pip install dotenv`
- Download mySQL (https://dev.mysql.com/downloads/installer/)
- Create a local .env file with the credentials listed in lines 10-16
- If uploading to git: create a .gitignore file with the text '.env' inside 


## How To Run the Program<a name="how-to-run"></a>
- Double click the 'run_script.bat' file


## FAQ<a name="faq"></a>
- This script will only post videos from the Lex Fridman channel which are podcast episodes (must have the text 'Lex Fridman Podcast #' in the title
- This script will check the last 20 posts on the subreddit, and if a post exists with the same video title (AKA if another user has already posted the video), then the video will not be posted to the subreddit
- To avoid spamming the actual Lex Fridman subreddit, a test subreddit was used when testing this script (the 'subreddit variable (line 99) must be edited before running the script)


## Troubleshooting<a name="troubleshooting"></a>
- If an error code at line 117 is thrown, it is likely due to issues with the Reddit authentification, so double-check the credentials are correct
- Ensure that the 'subreddit' variable has been edited before running script (the subreddit was not automatically entered to avoid accidentally spamming actual subreddit)


## Credits<a name="credits"></a>
Michelle Flandin
