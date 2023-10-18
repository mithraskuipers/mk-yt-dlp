import os
import subprocess

def run_scripts():
    # Ensure that the environment variables are set correctly
    os.environ['PATH'] += ":/usr/local/bin"
    os.environ['PYTHONPATH'] = os.getcwd()

    # List of script filenames in the desired order
    script_filenames = [
        "./scripts/install_aria2c.py",
        "./scripts/fetch_latest_yt-dlp_linux.py",
        "./scripts/copy_ytdlp_to_local_bin.py",
        "./scripts/make_conf_systemwide.py"
    ]

    # Get the current directory
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Python interpreter path
    python_interpreter = "/usr/bin/python3"  # Update this path if your Python interpreter is located elsewhere

    # Iterate over the script filenames and run them in order
    for script_filename in script_filenames:
        script_path = os.path.join(current_directory, script_filename)
        
        # Check if the script file exists
        if os.path.exists(script_path):
            try:
                # Run the script with sudo and the specified Python interpreter
                subprocess.run(["sudo", python_interpreter, script_path])
            except Exception as e:
                print(f"Error running {script_filename}: {e}")
        else:
            print(f"Error: {script_filename} not found.")

if __name__ == "__main__":
    # Check if the script is run with sudo privileges
    if os.geteuid() != 0:
        print("Error: This script requires sudo privileges to run.")
    else:
        # Run the scripts in the specified order
        run_scripts()
