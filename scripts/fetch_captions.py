from youtube_transcript_api import YouTubeTranscriptApi

def fetch_captions(video_id):
    try:
        # Fetch the transcript for the video
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        # Combine all text parts into a single string, removing line breaks
        captions_text = " ".join([entry['text'].replace("\n", " ") for entry in transcript])
        return "true", captions_text
    except Exception as e:
        print(f"Error fetching captions for video {video_id}: {e}")
        return "false", None
