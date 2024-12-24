# YouTube Data Scraper

## **Project Overview**
This project scrapes data from YouTube videos, including metadata, captions, and other key details. The output is stored in a CSV file with exactly 500 rows.

### **Features**
- Fetches top videos based on a user-specified genre.
- Collects video details such as URL, title, description, channel title, view count, and more.
- Downloads captions (if available) and includes them in the CSV.
- Ensures captions are sanitized to avoid issues with extra lines in the CSV.

---

## **Installation Instructions**

### **1. Clone the Repository**
```bash
git clone <repository_url>
cd youtube_data_scraper
```

### **2. Install Required Libraries**
Install all dependencies listed in the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### **3. Set Up API Key**
- Obtain a YouTube API Key from [Google Cloud Console](https://console.cloud.google.com/).
- Replace `YOUR_YOUTUBE_API_KEY` in `config/api_key.py` with your API key.

---

## **Usage Instructions**

### **1. Run the Script**
Execute the `main.py` file:
```bash
python main.py
```

### **2. Follow Prompts**
Enter the genre of videos you wish to scrape:
```
Enter the genre: technology
```

### **3. View Output**
The script will:
1. Fetch video IDs for the specified genre.
2. Collect video metadata.
3. Download captions (if available).
4. Save the data to `output.csv` in the `data/` folder.

---

## **Output**
The output CSV will include:
- Video URL
- Title
- Description
- Channel Title
- Keyword Tags
- YouTube Video Category
- Published Date
- Video Duration
- View Count
- Comment Count
- Captions (if available)
- Location of Recording (if available)

---

## **Troubleshooting**
1. **Quota Errors**: 
   - Ensure your API key has sufficient quota. You can create multiple API keys for higher limits.
2. **Captions Missing**:
   - Not all videos have captions enabled.
3. **Extra Rows in CSV**:
   - Ensure captions are sanitized by removing line breaks (`\n`).

---

## **Dependencies**
- `google-api-python-client`
- `pandas`
- `tqdm`
- `youtube-transcript-api`

Install these via:
```bash
pip install google-api-python-client pandas tqdm youtube-transcript-api
```

---

## **License**
This project is licensed under the MIT License. Feel free to modify and distribute as needed.