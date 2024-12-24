from googleapiclient.discovery import build
from config.api_key import API_KEY

def fetch_videos_by_genre(youtube, genre, max_results=500):
    video_ids = []
    next_page_token = None

    while len(video_ids) < max_results:
        request = youtube.search().list(
            q=genre,
            type="video",
            part="id",
            maxResults=min(50, max_results - len(video_ids)),
            pageToken=next_page_token
        )
        response = request.execute()
        for item in response['items']:
            video_ids.append(item['id']['videoId'])
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return video_ids[:max_results]