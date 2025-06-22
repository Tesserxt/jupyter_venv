import requests
import pandas as pd

API_KEY = "AIzaSyAcarihGjdbcvI4t0-CvMAePkYqdM39Y2Y"
CHANNEL_ID = "UCEk1jBxAl6fe-_G37G7huQA"  # Replace with the actual channel ID

# Get Channel Videos
def get_channel_videos(channel_id):
    url = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=50"
    response = requests.get(url).json()
    
    videos = []
    for item in response.get("items", []):
        if item["id"].get("videoId"):
            videos.append({
                "Video ID": item["id"]["videoId"],
                "Title": item["snippet"]["title"],
                "Published At": item["snippet"]["publishedAt"]
            })
    return videos

videos_data = get_channel_videos(CHANNEL_ID)

# Save to CSV
df = pd.DataFrame(videos_data)
df.to_csv("youtube_channel_videos.csv", index=False)

print("CSV file saved!")
