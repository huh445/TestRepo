import requests
import json

class GetVid:
    def __init__(self,):
        self.api_key = "AIzaSyBlNPs3mZvPBxk4roKQO5tLYPMxZy3sLx4"
        self.channel_id = "UCsSsgPaZ2GSmO6il8Cb5iGA"

    def get_vid(self):
        # Construct the API request
        api_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={self.channel_id}&maxResults=1&order=date&type=video&key={self.api_key}"

        # Send the request
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an exception for bad response codes
            data = response.json()

            if "items" in data and len(data["items"]) > 0:
                latest_video = data["items"][0]
                video_id = latest_video["id"]["videoId"]
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                return video_url
            else:
                print("No video found in API response")
                return None, None

        except requests.exceptions.RequestException as e:
            print(f"Error fetching API data: {e}")
            return None, None

