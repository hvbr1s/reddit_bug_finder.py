import csv
import praw
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

env_vars = [
    'CLIENT_ID',
    'CLIENT_SECRET',
    'USER_AGENT',
]

# Create a Reddit instance with your app credentials
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT")
)

# Define the subreddit
subreddit = reddit.subreddit('ledgerwallet')

# Get the date n days ago
seven_days_ago = datetime.utcnow() - timedelta(days=2)

# Get today's date as a string
today = datetime.today().strftime('%Y_%m_%d')

# Open a CSV file to write the data
with open(f'reddit.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Title', 'Score', 'URL', 'Created', 'Content'])

    # Get the top posts from the last 7 days
    for post in subreddit.new(limit=1000):  # adjust the limit as needed
        if datetime.utcfromtimestamp(post.created_utc) > seven_days_ago:
            # Write the post data to the CSV
            writer.writerow([post.title, post.score, post.url, post.created, post.selftext])

######## MOVING FILE BACK TO WINDOWS ######
# cp /home/dan/reddit_sentiment/reddit.csv /mnt/c/Users/ejahe/Desktop/ 
