import os
import shutil

def copy_latest_yt_dlp_config():
    # Source directory where yt-dlp_rpi.conf is located
    source_directory = os.path.join(os.getcwd(), "configs")

    # Source path for yt-dlp_rpi.conf
    source_config_path = os.path.join(source_directory, "yt-dlp_rpi.conf")

    # Destination path for yt-dlp_rpi.conf in /etc directory
    destination_path = "/etc/yt-dlp_rpi.conf"

    try:
        # Copy the yt-dlp_rpi.conf file to /etc/yt-dlp_rpi.conf
        shutil.copy2(source_config_path, destination_path)

        print(f"yt-dlp_rpi.conf copied to {destination_path}.")
    except Exception as e:
        print(f"Error: {e}")

# Call the function to copy yt-dlp_rpi.conf
copy_latest_yt_dlp_config()
