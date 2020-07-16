import praw
from config_handler import ScrapingConfig

def main():
    config_handler = ScrapingConfig()
    client_id = config_handler.client_id
    client_secret = config_handler.client_secret
    user_agent = config_handler.user_agent

    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
    hot_posts = reddit.subreddit('F1Porn').hot(limit=10)

    for post in hot_posts:
        print(post.title)    

if __name__ == "__main__":
    main()