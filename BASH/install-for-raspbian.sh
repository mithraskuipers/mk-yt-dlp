#!/bin/bash

sudo apt install ffmpeg -y ;

# Variables for paths and URLs
LATEST_RELEASE_URL="https://api.github.com/repos/yt-dlp/yt-dlp/releases/latest"
DOWNLOAD_DIR="$(pwd)"
YTDLP_BINARY="yt-dlp_linux"
INSTALL_PATH="/usr/local/bin"
CFG_FILES_DIR="./cfg-files"
TARGET_CFG_DIR="/etc"
BASHRC_PATH="$HOME/.bashrc"

# Inform the user about each step
echo "Fetching the latest release information from GitHub..."

# Get the download URL for the yt-dlp binary from the latest release
DOWNLOAD_URL=$(curl -s "$LATEST_RELEASE_URL" | grep -Eo '"browser_download_url":\s*"[^"]*yt-dlp"' | cut -d '"' -f 4)

# Check if the download URL was found
if [ -z "$DOWNLOAD_URL" ]; then
  echo "Failed to find the download URL for yt-dlp. Please check the GitHub page."
  exit 1
fi

echo "Downloading yt-dlp from: $DOWNLOAD_URL..."
# Download the yt-dlp binary to the current directory
curl -L "$DOWNLOAD_URL" -o "$DOWNLOAD_DIR/$YTDLP_BINARY"

if [ ! -f "$DOWNLOAD_DIR/$YTDLP_BINARY" ]; then
  echo "Failed to download yt-dlp. Exiting."
  exit 1
fi

echo "Download completed. Making the yt-dlp binary executable..."
# Make the yt-dlp binary executable
chmod a+x "$DOWNLOAD_DIR/$YTDLP_BINARY"

echo "Copying yt-dlp to $INSTALL_PATH and renaming it..."
# Copy and rename the yt-dlp binary to /usr/local/bin
sudo cp "$DOWNLOAD_DIR/$YTDLP_BINARY" "$INSTALL_PATH/yt-dlp"
if [ $? -eq 0 ]; then
  echo "yt-dlp has been successfully installed to $INSTALL_PATH as yt-dlp."
else
  echo "Failed to copy yt-dlp to $INSTALL_PATH. Please check permissions."
  exit 1
fi

echo "Copying configuration files from $CFG_FILES_DIR to $TARGET_CFG_DIR..."
# Copy configuration files
if [ -d "$CFG_FILES_DIR" ]; then
  sudo cp "$CFG_FILES_DIR"/* "$TARGET_CFG_DIR"/
  echo "Configuration files have been copied to $TARGET_CFG_DIR."
else
  echo "Configuration folder $CFG_FILES_DIR not found. Skipping config copy."
fi

# Adding aliases to ~/.bashrc
echo "Adding aliases to $BASHRC_PATH..."
ALIAS_LINE1="alias ytva='yt-dlp --config-location /etc/yt-dlp-rpi.conf'"
ALIAS_LINE2="alias yta='yt-dlp --config-location /etc/yt-dlp-rpi-audio.conf'"
ALIAS_LINE3="alias yt-dlp='yt-dlp'"
ALIAS_LINE4="alias ytval='yt-dlp --config-location /etc/yt-dlp-rpi.conf -a urls.txt'"

if ! grep -q "$ALIAS_LINE1" "$BASHRC_PATH"; then
  echo "$ALIAS_LINE1" >> "$BASHRC_PATH"
fi
if ! grep -q "$ALIAS_LINE2" "$BASHRC_PATH"; then
  echo "$ALIAS_LINE2" >> "$BASHRC_PATH"
fi
if ! grep -q "$ALIAS_LINE3" "$BASHRC_PATH"; then
  echo "$ALIAS_LINE3" >> "$BASHRC_PATH"
fi
if ! grep -q "$ALIAS_LINE4" "$BASHRC_PATH"; then
  echo "$ALIAS_LINE4" >> "$BASHRC_PATH"
fi

echo "Aliases added to $BASHRC_PATH. To use them immediately, run: source $BASHRC_PATH"

# Inform the user that the process is complete
echo "yt-dlp setup completed successfully."

