import os
import shutil

def move_ytdlp_binary():
    # Source path (yt-dlp binary in latest_yt-dlp folder)
    source_path = os.path.join(os.getcwd(), "latest_yt-dlp", "yt-dlp")
    
    # Destination path
    destination_path = os.path.expanduser("/usr/local/bin")
    
    try:
        # Create the ~/.local/bin directory if it doesn't exist
        os.makedirs(destination_path, exist_ok=True)
        
        # Destination path with the new binary name
        destination_binary_path = os.path.join(destination_path, "yt-dlp")
        
        # Copy the yt-dlp binary and rename it to yt-dlp
        shutil.copy2(source_path, destination_binary_path)
        
        # Set execute permissions for the copied binary
        os.chmod(destination_binary_path, 0o755)  # Sets the binary to be executable
        
        print("yt-dlp binary copied to ~/.local/bin and made executable.")
    except Exception as e:
        print(f"Error: {e}")

# Call the function to move and rename the binary
move_ytdlp_binary()