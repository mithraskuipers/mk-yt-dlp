#!/bin/bash

# Define the alias and command
alias_name="ytva"
command="yt-dlp --config-location /etc/yt-dlp-linux.conf"
# Get the current user's home directory
home_directory="$HOME"
bashrc_file="$home_directory/.bashrc"

# Check if the alias already exists in .bashrc
if grep -q "alias $alias_name=" "$bashrc_file"; then
    echo "Alias '$alias_name' already exists in $bashrc_file."
else
    # Add the alias to .bashrc
    echo -e "\n# Alias for using yt-dlp_linux with custom config" >> "$bashrc_file"
    echo "alias $alias_name='$command'" >> "$bashrc_file"
    echo "Alias '$alias_name' added to $bashrc_file."
    # Apply the alias in the current shell session
    alias $alias_name="$command"
fi

# Source the .bashrc file to apply the changes in the current session
source "$bashrc_file"

# Display the path of the file where the alias has been added
echo "Alias '$alias_name' added to $bashrc_file and sourced for the current session."
