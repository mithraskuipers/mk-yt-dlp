#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

# Select system type (simplified to only handle Linux)
select_system_type() {
  echo "Select your operating system:"
  echo "1. Linux"
  echo "(Note: Raspberry Pi option is ignored in this version)"
  while true; do
    read -p "Enter your choice (1 for Linux): " choice
    if [[ "$choice" == "1" ]]; then
      echo "linux"
      return
    else
      echo "Invalid choice. Please try again."
    fi
  done
}

# Install aria2c
install_aria2c() {
  echo "Installing aria2c..."
  sudo apt-get update
  sudo apt-get install -y aria2
}

# Fetch the latest yt-dlp for Linux
fetch_latest_ytdlp_linux() {
  echo "Fetching the latest yt-dlp for Linux..."
  local url
  local output_path="$(pwd)/latest_yt-dlp_linux/yt-dlp_linux"
  mkdir -p "$(pwd)/latest_yt-dlp_linux"

  url=$(curl -s https://github.com/yt-dlp/yt-dlp/releases | grep -oP '/yt-dlp/yt-dlp/releases/download/\K([0-9]+\.[0-9]+\.[0-9]+)/yt-dlp_linux' | head -n 1)

  if [[ -z "$url" ]]; then
    echo "Failed to find the latest Linux release."
    exit 1
  fi

  full_url="https://github.com/yt-dlp/yt-dlp/releases/download/${url}/yt-dlp_linux"
  echo "Downloading from $full_url"

  if [[ -f "$output_path" ]]; then
    echo "Removing old yt-dlp_linux file."
    rm "$output_path"
  fi

  curl -L "$full_url" -o "$output_path"
  chmod +x "$output_path"
  echo "Download completed. File saved in 'latest_yt-dlp_linux' subfolder."
}

# Copy yt-dlp to /usr/local/bin
copy_ytdlp_linux_to_local_bin() {
  echo "Copying yt-dlp to /usr/local/bin..."
  local source_path="$(pwd)/latest_yt-dlp_linux/yt-dlp_linux"
  local destination_path="/usr/local/bin/yt-dlp"

  sudo cp "$source_path" "$destination_path"
  sudo chmod 755 "$destination_path"
  echo "yt-dlp binary copied to /usr/local/bin and made executable."
}

# Add yt-dlp config to /etc
add_conf_linux() {
  echo "Adding yt-dlp config to /etc..."
  local source_config_path="$(pwd)/configs/yt-dlp-linux.conf"
  local destination_path="/etc/yt-dlp-linux.conf"

  if [[ ! -f "$source_config_path" ]]; then
    echo "Error: Config file $source_config_path not found."
    exit 1
  fi

  sudo cp "$source_config_path" "$destination_path"
  echo "yt-dlp_linux.conf copied to $destination_path."
}

# Main execution
main() {
  local system_type
  system_type=$(select_system_type)

  if [[ "$system_type" == "linux" ]]; then
    install_aria2c
    fetch_latest_ytdlp_linux
    copy_ytdlp_linux_to_local_bin
    add_conf_linux
  fi
}

main
