import os
import requests
import re
import wget

def get_latest_ytdlp_release():
    url = "https://github.com/yt-dlp/yt-dlp/releases"
    response = requests.get(url)
    
    if response.status_code == 200:
        page_content = response.text
        pattern = r'/yt-dlp/yt-dlp/releases/download/(\d+\.\d+\.\d+)/yt-dlp_linux'
        match = re.search(pattern, page_content)
        if match:
            release_version = match.group(1)
            download_url = f"https://github.com/yt-dlp/yt-dlp/releases/download/{release_version}/yt-dlp_linux"
            return download_url
        else:
            print("No Linux release found.")
    else:
        print("Failed to fetch release information.")

# Create a subfolder for the downloaded file
download_folder = os.path.join(os.getcwd(), "latest_yt-dlp_linux")
os.makedirs(download_folder, exist_ok=True)

# Set the output path to the subfolder
output_path = os.path.join(download_folder, "yt-dlp_linux")

# Check if the file already exists, and remove it if it does
if os.path.exists(output_path):
    os.remove(output_path)
    print("Previous yt-dlp_linux file removed.")

# Download the latest yt-dlp Linux release
latest_release_url = get_latest_ytdlp_release()
if latest_release_url:
    print("Downloading latest yt-dlp Linux release...")
    try:
        wget.download(latest_release_url, output_path)
        print("\nDownload completed. File saved in 'latest_yt-dlp_linux' subfolder.")
    except Exception as e:
        print(f"Download failed: {e}")
else:
    print("Failed to retrieve the latest yt-dlp Linux release.")
