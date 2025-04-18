import os
import subprocess
import sys

def run_scripts(system_type):
    # Ensure that the environment variables are set correctly
    os.environ['PATH'] += ":/usr/local/bin"
    os.environ['PYTHONPATH'] = os.getcwd()

    python_interpreter = sys.executable  # Get the path of the Python interpreter

    # Define script paths based on the provided system type
    if system_type == "rpi":
        fetch_ytdlp_script = "./scripts/fetch_latest_yt-dlp.py"
        copy_ytdlp_script = "./scripts/copy_ytdlp_to_local_bin.py"
        add_conf = "./scripts/add_conf.py"
    else:
        fetch_ytdlp_script = "./scripts/fetch_latest_yt-dlp_linux.py"
        copy_ytdlp_script = "./scripts/copy_ytdlp_linux_to_local_bin.py"
        add_conf = "./scripts/add_conf_linux.py"

    # List of script filenames in the desired order
    script_filenames = [
        "./scripts/install_aria2c.py",
        fetch_ytdlp_script,
        copy_ytdlp_script,
        add_conf
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

def select_system_type():
    print("Select your operating system:")
    print("1. Linux")
    print("2. Raspberry Pi (Raspbian)")
    
    while True:
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            return "linux"
        elif choice == '2':
            return "rpi"
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Prompt user to select the system type
    system_type = select_system_type()
    
    # Run the scripts in the specified order
    run_scripts(system_type)

