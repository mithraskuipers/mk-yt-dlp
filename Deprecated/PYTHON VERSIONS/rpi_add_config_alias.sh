#!/bin/bash

# Define aliases and their respective commands
alias_name_audio="yta"
command_audio="yt-dlp --config-location /etc/yt-dlp-rpi-audio.conf"
alias_name_videoaudio="ytva"
command_videoaudio="yt-dlp --config-location /etc/yt-dlp-rpi-videoaudio.conf"

# Get the current user's home directory
home_directory="$HOME"
bashrc_file="$home_directory/.bashrc"

# Function to add alias if it doesn't already exist
add_alias() {
    local alias_name="$1"
    local command="$2"

    # Check if the alias already exists in .bashrc
    if grep -q "alias $alias_name=" "$bashrc_file"; then
        echo "Alias '$alias_name' already exists in $bashrc_file."
    else
        # Add the alias to .bashrc
        echo -e "\n# Alias for using yt-dlp with $alias_name config" >> "$bashrc_file"
        echo "alias $alias_name='$command'" >> "$bashrc_file"
        echo "Alias '$alias_name' added to $bashrc_file."
        # Apply the alias in the current shell session
        alias $alias_name="$command"
    fi
}

# Add aliases for both audio and video configurations
add_alias "$alias_name_audio" "$command_audio"
add_alias "$alias_name_videoaudio" "$command_videoaudio"

# Display confirmation
echo "Aliases '$alias_name_audio' and '$alias_name_videoaudio' added to $bashrc_file."
