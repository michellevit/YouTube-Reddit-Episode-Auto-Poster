Project Title: YouTube-Reddit Auto Post Script 


----------
Table of Contents: 
1. Project Description
2. Requirements
3. Installation
4. Resources
5. How to Run the Program
6. Troubleshooting
7. FAQ
8. Credits


----------
1. Project Description

This Python script checks the Lex Fridman YouTube channel for the latest podcast episode, and posts the video to the Lex Fridman subreddit (if it has not already been posted).

*Note: to avoid spamming the actual Lex Fridman subreddit, a test subreddit was used when testing this script (the 'subreddit variable (line 99) must be edited before running the script)


----------
2. Requirements

Libraries: 
-Python 3.9 or higher
-googleapiclient
-mysql.connector
-praw
-os
-dotenv
Other:
-pip
-a google account
-a YouTube API key
-a reddit account
-a reddit API key
-mySQL Workbench


----------
3. Installation:

-Install Python 3.9.13 or higher
-Create Virtual Environment (https://www.youtube.com/watch?v=APOPm01BVrk&t=0s) : 
-- open terminal
-- cd into folder
-- create Python environment: python -m venv project_yt_api
-- activate the virtual environment: project_yt_api\Scripts\activate.bat
-- install google api: project_yt_api\Scripts\pip.exe install google-api-python-client
--install mysql.connector: pip install mysql.connector
--install praw: pip install praw
-install dotenv: pip install dotenv
-Download mySQL (https://dev.mysql.com/downloads/installer/)
-Create a local .env file with the credentials listed in lines 10-16
-if uploading to git: create a .gitignore file with the text '.env' inside 


----------
4. Resources: 

Google/YT API Documentation: https://github.com/googleapis/google-api-python-client
YouTube API: https://developers.google.com/youtube/v3
How to set-up virtual environment: https://www.youtube.com/watch?v=APOPm01BVrk&t=0s
Python YouTube API Tutorial: https://www.youtube.com/watch?v=th5_9woFJmk
mySQL Tutorial (setup + basic queries): https://www.youtube.com/watch?v=3vsC05rxZ8c


----------
5. How to Run the Program: 

Double click the 'run_script.bat' file


----------
6. Troubleshooting: 
* If an error code at line 117 is thrown, it is likely due to issues with the Reddit authentification, so double-check the credentials are correct


----------
7. FAQ

-This script will only post videos from the Lex Fridman channel which are podcast episodes (must have the text 'Lex Fridman Podcast #' in the title
-This script will check the last 20 posts on the subreddit, and if a post exists with the same video title (AKA if another user has already posted the video), then the video will not be posted to the subreddit


----------
8. Credits

Michelle Flandin
