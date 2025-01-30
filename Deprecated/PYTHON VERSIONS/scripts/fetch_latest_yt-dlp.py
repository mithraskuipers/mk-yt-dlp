import os
import requests
import re

def download_file(url, output_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return True
    return False

def get_latest_ytdlp_release():
    url = "https://github.com/yt-dlp/yt-dlp/releases"
    response = requests.get(url)
    
    if response.status_code == 200:
        page_content = response.text
        pattern = r'/yt-dlp/yt-dlp/releases/download/(\d+\.\d+\.\d+)/yt-dlp'
        match = re.search(pattern, page_content)
        if match:
            release_version = match.group(1)
            download_url = f"https://github.com/yt-dlp/yt-dlp/releases/download/{release_version}/yt-dlp"
            return download_url
        else:
            print("No Linux release found.")
    else:
        print("Failed to fetch release information.")

# Create a subfolder for the downloaded file
download_folder = os.path.join(os.getcwd(), "latest_yt-dlp")
os.makedirs(download_folder, exist_ok=True)

# Set the output path to the subfolder
output_path = os.path.join(download_folder, "yt-dlp")

# Check if the file already exists, and remove it if it does
if os.path.exists(output_path):
    os.remove(output_path)
    print("Previous yt-dlp file removed.")

# Download the latest yt-dlp Linux release
latest_release_url = get_latest_ytdlp_release()
if latest_release_url:
    print("Downloading latest yt-dlp Linux release...")
    try:
        if download_file(latest_release_url, output_path):
            print("\nDownload completed. File saved in 'latest_yt-dlp' subfolder.")
        else:
            print("\nDownload failed.")
    except Exception as e:
        print(f"Download failed: {e}")
else:
    print("Failed to retrieve the latest yt-dlp Linux release.")
