import os
import subprocess
import sys

def run_scripts():
    # Ensure that the environment variables are set correctly
    os.environ['PATH'] += ":/usr/local/bin"
    os.environ['PYTHONPATH'] = os.getcwd()

    python_interpreter = sys.executable  # Get the path of the Python interpreter

    # List of script filenames in the desired order
    script_filenames = [
        "./scripts/install_aria2c.py",
        "./scripts/fetch_latest_yt-dlp_linux.py",
        "./scripts/copy_ytdlp_to_local_bin.py",
        "./scripts/add_conf.py",
        "./scripts/add_mp3_conf.py"
        ]

    # Get the current directory
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Iterate over the script filenames and run them in order
    for script_filename in script_filenames:
        script_path = os.path.join(current_directory, script_filename)

        # Check if the script file exists
        if os.path.exists(script_path):
            try:
                # Grant execute permission to the shell script
                subprocess.run(["chmod", "+x", script_path])
                # Run other scripts with the specified Python interpreter
                subprocess.run([python_interpreter, script_path])
            except Exception as e:
                print(f"Error running {script_filename}: {e}")
        else:
            print(f"Error: {script_filename} not found.")

if __name__ == "__main__":
    # Run the scripts in the specified order without sudo
    run_scripts()
