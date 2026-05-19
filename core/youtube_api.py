from googleapiclient.discovery import build
import re

API_KEY = "blablabla"  # <- Replace with your API key
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)


def get_video_id(url):
    """
    Extracts the video ID from a YouTube URL
    """
    match = re.search(r"v=([a-zA-Z0-9_-]{11})", url)
    if match:
        return match.group(1)
    match = re.search(r"youtu\.be/([a-zA-Z0-9_-]{11})", url)
    if match:
        return match.group(1)
    raise ValueError("Invalid YouTube URL")


def fetch_comments(video_url, count=50):
    """
    Fetch comments from a YouTube video, handling pagination.
    Returns a list of comment texts.
    """
    video_id = get_video_id(video_url)
    comments = []
    next_page_token = None

    while len(comments) < count:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=min(100, count - len(comments)),  
            pageToken=next_page_token,
            textFormat="plainText"
        )
        response = request.execute()

        for item in response.get("items", []):
            comment_text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment_text)

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return comments[:count]
