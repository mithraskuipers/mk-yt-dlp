import os
import shutil

def copy_latest_yt_dlp_config():
    # Source directory where the config files are located
    source_directory = os.path.join(os.getcwd(), "configs")

    # Source paths for the specific config files
    source_config_audio_path = os.path.join(source_directory, "yt-dlp-rpi-audio.conf")
    source_config_videoaudio_path = os.path.join(source_directory, "yt-dlp-rpi-videoaudio.conf")

    # Destination paths for the config files in /etc directory
    destination_audio_path = "/etc/yt-dlp-rpi-audio.conf"
    destination_videoaudio_path = "/etc/yt-dlp-rpi-videoaudio.conf"

    try:
        # Copy the yt-dlp-rpi-audio.conf file to /etc
        shutil.copy2(source_config_audio_path, destination_audio_path)
        print(f"yt-dlp-rpi-audio.conf copied to {destination_audio_path}.")

        # Copy the yt-dlp-rpi-videoaudio.conf file to /etc
        shutil.copy2(source_config_videoaudio_path, destination_videoaudio_path)
        print(f"yt-dlp-rpi-videoaudio.conf copied to {destination_videoaudio_path}.")
        
    except Exception as e:
        print(f"Error: {e}")

# Call the function to copy the config files
copy_latest_yt_dlp_config()
