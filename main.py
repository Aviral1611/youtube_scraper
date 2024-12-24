from utils.youtube_client import get_youtube_client
from scripts.fetch_videos import fetch_videos_by_genre
from scripts.fetch_details import fetch_video_details
from scripts.fetch_captions import fetch_captions
from scripts.save_to_csv import save_to_csv
from tqdm import tqdm

if __name__ == "__main__":
    youtube = get_youtube_client()
    genre = input("Enter the genre: ")

    print("Fetching video IDs...")
    video_ids = fetch_videos_by_genre(youtube, genre)

    print("Fetching video details...")
    video_data = fetch_video_details(youtube, video_ids)

    print("Checking captions and downloading...")
    for video in tqdm(video_data, desc="Fetching captions"):
        captions_available, captions_text = fetch_captions(video['Video URL'].split("=")[-1])
        video["Captions Available"] = captions_available
        video["Caption Text"] = captions_text

    print("Saving data to CSV...")
    save_to_csv(video_data)