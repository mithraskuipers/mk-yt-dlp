import os
import shutil

def move_ytdlp_binary():
    # Source path (yt-dlp_linux binary in latest_yt-dlp_linux folder)
    source_path = os.path.join(os.getcwd(), "latest_yt-dlp_linux", "yt-dlp_linux")
    
    # Destination path (~/.local/bin directory)
    destination_path = os.path.expanduser("~/.local/bin/")
    
    try:
        # Create the ~/.local/bin directory if it doesn't exist
        os.makedirs(destination_path, exist_ok=True)
        
        # Copy the yt-dlp_linux binary to ~/.local/bin directory
        shutil.copy2(source_path, destination_path)
        
        # Set execute permissions for the copied binary
        binary_path = os.path.join(destination_path, "yt-dlp_linux")
        os.chmod(binary_path, 0o755)  # Sets the binary to be executable
        
        print("yt-dlp_linux binary copied to ~/.local/bin and made executable.")
    except Exception as e:
        print(f"Error: {e}")

# Call the function to move the binary
move_ytdlp_binary()
