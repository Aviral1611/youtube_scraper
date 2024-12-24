from googleapiclient.discovery import build
from config.api_key import API_KEY

def get_youtube_client():
    return build("youtube", "v3", developerKey=API_KEY)