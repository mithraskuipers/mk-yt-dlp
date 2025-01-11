import yt_dlp
import sys

def search_youtube(query):
    # Configure yt-dlp options
    ydl_opts = {
        'quiet': True,  # Don't print messages
        'default_search': 'ytsearch500',  # Search YouTube and return up to 500 results
        'noplaylist': True,  # Only search for videos
        'extract_flat': True,  # Only extract video info (don't download)
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Use yt-dlp to search for the query, fetching up to 500 results
        search_results = ydl.extract_info(f"ytsearch500:{query}", download=False)

    video_urls = []

    for entry in search_results['entries']:
        # Check if the search string is found anywhere in the title (case-insensitive)
        if query.lower() in entry['title'].lower():
            video_urls.append(entry['url'])

    return video_urls


if __name__ == "__main__":
    # Check if the search string was provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python yt-url-getter.py '<search_string>'")
        sys.exit(1)

    # Get the search string from command-line argument
    search_string = sys.argv[1].strip()

    # Search for videos
    videos = search_youtube(search_string)

    # Print the number of found URLs
    print(f"Found {len(videos)} URLs:")

    # Print all video URLs, space-separated
    if videos:
        print("\n" + " ".join(videos))
    else:
        print(f"No videos found with '{search_string}' in the title.")
