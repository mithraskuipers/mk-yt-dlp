import os
import shutil

def copy_latest_yt_dlp_config():
    # Source directory where yt-dlp.conf is located
    source_directory = os.path.join(os.getcwd(), "latest_yt-dlp_configs")

    # Source path for yt-dlp.conf
    source_config_path = os.path.join(source_directory, "yt-dlp_mp3.conf")

    # Destination path for yt-dlp.conf in /etc directory
    destination_path = "/etc/yt-dlp_mp3.conf"

    try:
        # Copy the yt-dlp.conf file to /etc/yt-dlp.conf
        shutil.copy2(source_config_path, destination_path)

        print(f"yt-dlp_mp3.conf copied to {destination_path}.")
    except Exception as e:
        print(f"Error: {e}")

# Call the function to copy yt-dlp.conf
copy_latest_yt_dlp_config()
