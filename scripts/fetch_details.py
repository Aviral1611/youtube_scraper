from tqdm import tqdm

def fetch_video_details(youtube, video_ids):
    video_details = []

    for i in tqdm(range(0, len(video_ids), 50), desc="Fetching video details"):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics,recordingDetails",
            id=",".join(video_ids[i:i+50])
        )
        response = request.execute()
        for video in response['items']:
            location = video.get('recordingDetails', {}).get('location', {})
            details = {
                "Video URL": f"https://www.youtube.com/watch?v={video['id']}",
                "Title": video['snippet']['title'],
                "Description": video['snippet']['description'],
                "Channel Title": video['snippet']['channelTitle'],
                "Keyword Tags": video['snippet'].get('tags', []),
                "YouTube Video Category": video['snippet'].get('categoryId', 'N/A'),
                "Video Published at": video['snippet']['publishedAt'],
                "Video Duration": video['contentDetails']['duration'],
                "View Count": video['statistics'].get('viewCount', 0),
                "Comment Count": video['statistics'].get('commentCount', 0),
                "Captions Available": "false",  # Will update later
                "Location of Recording": f"{location.get('latitude', 'N/A')}, {location.get('longitude', 'N/A')}" if location else "N/A",
            }
            video_details.append(details)
    return video_details
