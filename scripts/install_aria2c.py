import subprocess

def install_aria2():
    try:
        # Run the apt-get install command with sudo
        subprocess.run(["sudo", "apt-get", "install", "aria2", "-y"])
        print("aria2 has been installed successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Call the function to install aria2
install_aria2()
