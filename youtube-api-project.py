from googleapiclient.discovery import build
import mysql.connector
import praw
import os
from dotenv import load_dotenv


# CREDENTIALS (in .env file, and ignored by git with .gitignore file): 
load_dotenv()
yt_api_key = os.getenv("yt_api_key")
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
reddit_client_id = os.getenv("reddit_client_id")
reddit_client_secret = os.getenv("reddit_client_secret")
reddit_username = os.getenv("reddit_username")
reddit_password = os.getenv("reddit_password")


# GET YOUTUBE VIDEO DATA

youtube = build('youtube', 'v3', developerKey=yt_api_key) 

yt_channel_id = 'UCSHZKyawb77ixDdsGog4iWA'


# VIDEO DATA USING ACTUAL YOUTUBE DATA API REQUESTS

search_response = youtube.search().list(part="id",
                                            type='video',
                                            order='date',
                                            channelId=yt_channel_id,
                                            maxResults=1).execute()

video_id = search_response['items'][0]['id']['videoId']

video_url = "https://www.youtube.com/watch?v=" + video_id

videos_response = youtube.videos().list(part="snippet", id=video_id).execute()

video_date = (videos_response['items'][0]['snippet']['publishedAt'])[0:9]

video_title = videos_response['items'][0]['snippet']['title']


## TEST DATA (SO YOU DON'T EXCEED REQUEST QUOTA WITH YOUTUBE DATA API)

# video_id = "SK4kMPmgKW8"
# video_title = "Christopher Capozzola: World War I, Ideology, 'Propaganda, and Politics | Lex Fridman Podcast #320"
# video_date = "2022-09-14"
# video_url = "https://www.youtube.com/watch?v=" + video_id


# GET EPISODE NUMBER

if video_title.find('#'):
    location_of_hash = video_title.find('#')
    episode_number = ''
    for x in range(1,5):
        if (location_of_hash + x) < len(video_title): 
            if video_title[location_of_hash + x].isnumeric():
                number_to_add = video_title[location_of_hash + x]
                episode_number += number_to_add


# CREATE CONNECTION TO DATABASE

db = mysql.connector.connect(
    host="localhost",
    user=db_user,
    passwd=db_password,
    database="uploaded_videos_database"
)


## Create a Cursor
mycursor = db.cursor()

## Create database (if it does not already exist)
mycursor.execute("CREATE DATABASE IF NOT EXISTS uploaded_videos_database")

## Create a table (if it does not already exist)
mycursor.execute("CREATE TABLE IF NOT EXISTS Videos (date VARCHAR(10), youtubeID VARCHAR(25), title VARCHAR(255), episodeNum int UNSIGNED,videoID int PRIMARY KEY AUTO_INCREMENT)")

query_check = "SELECT * FROM Videos WHERE youtubeID = (%s)"
value_check = video_id
mycursor.execute(query_check, (value_check,))
myresult = mycursor.fetchall()

## Reddit Credentials
reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent="post bot",
    username=reddit_username,
    password=reddit_password
)

## Get subreddit
subreddit = reddit.subreddit("")

## Check to make sure user has entered a subreddit
if subreddit == "":
  console.log("Error - No Subreddit: please enter a subreddit (on line 99) before running this script")
 

## Add to database and post onto subreddit, if the episode has not already been added to the database or posted to the subreddit
if len(myresult) >= 1:
    print("ERROR: Podcast episode #{} is already in the database".format(episode_number))
elif "Lex Fridman Podcast #" not in video_title:
    print("ERROR: The latest video that was posted was not a podcast episode")
else: 
    mycursor.execute("INSERT INTO Videos (date, youtubeID, title, episodeNum) VALUES (%s,%s,%s,%s)", (video_date, video_id, video_title, episode_number))
    db.commit()
    print("Podcast episode #{} has been entered into the database table".format(episode_number))
    # Check if episode has already been posted to subreddit, and if not, post it
    last_ten_posts = subreddit.new(limit=10)
    post_checker = 0
    for post in last_ten_posts:
        print(post.title)
        if video_title in post.title:
            print("ERROR: Podcast episode #{} has already been uploaded to subreddit by another user".format(episode_number))
            post_checker = 1
            break
    if post_checker == 0: 
        subreddit.submit(video_title,url=video_url)
        print("New podcast episode #{} has been posted to the {} subreddit".format(episode_number, subreddit))


# CODE FOR TESTING + TROUBLESHOOTING

## Print all records from table:
# mycursor.execute("SELECT * FROM Videos")
# result = mycursor.fetchall()
# print("Table Data: ")
# for row in result:
#     print(row)

## Clear data from Table
#mycursor.execute("TRUNCATE TABLE Videos")

## Delete table entirely
#mycursor.execute("DROP TABLE Videos")
