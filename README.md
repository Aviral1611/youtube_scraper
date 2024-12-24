YouTube Data Scraper
Project Overview
This project scrapes data from YouTube videos, including metadata, captions, and other key details. The output is stored in a CSV file with exactly 500 rows.

Features
Fetches top videos based on a user-specified genre.
Collects video details such as URL, title, description, channel title, view count, and more.
Downloads captions (if available) and includes them in the CSV.
Ensures captions are sanitized to avoid issues with extra lines in the CSV.
Installation Instructions
1. Clone the Repository
bash
Copy code
git clone <repository_url>
cd youtube_data_scraper
2. Install Required Libraries
Install all dependencies listed in the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
3. Set Up API Key
Obtain a YouTube API Key from Google Cloud Console.
Replace YOUR_YOUTUBE_API_KEY in config/api_key.py with your API key.
Usage Instructions
1. Run the Script
Execute the main.py file:

bash
Copy code
python main.py
2. Follow Prompts
Enter the genre of videos you wish to scrape:

mathematica
Copy code
Enter the genre: technology
3. View Output
The script will:

Fetch video IDs for the specified genre.
Collect video metadata.
Download captions (if available).
Save the data to output.csv in the data/ folder.
Output
The output CSV will include:

Video URL
Title
Description
Channel Title
Keyword Tags
YouTube Video Category
Published Date
Video Duration
View Count
Comment Count
Captions (if available)
Location of Recording (if available)
Troubleshooting
Quota Errors:
Ensure your API key has sufficient quota. You can create multiple API keys for higher limits.
Captions Missing:
Not all videos have captions enabled.
Extra Rows in CSV:
Ensure captions are sanitized by removing line breaks (\n).
Dependencies
google-api-python-client
pandas
tqdm
youtube-transcript-api
Install these via:

bash
Copy code
pip install google-api-python-client pandas tqdm youtube-transcript-api
License
This project is licensed under the MIT License. Feel free to modify and distribute as needed.
