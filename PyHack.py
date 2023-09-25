import subprocess
import sys
import os

def check_dependency(package):
    try:
        dist = subprocess.check_output([sys.executable, "-m", "pip", "show", package])
        if dist:
            return True
    except Exception:
        return False

def install_dependency(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def update_pip():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

def check_pip():
    try:
        pip_version = subprocess.check_output([sys.executable, "-m", "pip", "--version"])
        if pip_version:
            return True
    except Exception:
        return False

def run_script(script_path):
    os.system(f'python3 {script_path}')

def main():
    dependencies = ["scapy", "argparse", "socket", "shlex", "subprocess", "sys", "textwrap", "threading"]
    all_installed = True

    if not check_pip():
        print("pip is not installed. Please install pip first.")
        return

    print("Checking for pip updates...")
    update_pip()

    for dep in dependencies:
        if not check_dependency(dep):
            print(f"Dependency {dep} is not installed.")
            all_installed = False

    if all_installed:
        print("All dependencies are installed.")
        print("Which script do you want to run?")
        print("1. Net_Crawler/main.py")
        print("2. Net_Hunter/main.py")
        answer = input()
        if answer == "1":
            run_script('Net_Crawler/main.py')
        elif answer == "2":
            run_script('Net_Hunter/main.py')
        else:
            print("Invalid option. Please enter 1 or 2.")
    else:
        print("In order for PyHack to run correctly, please install all the vital dependencies!")
        print("Do you want to install missing dependencies now? (yes/no)")
        answer = input()
        if answer.lower() == "yes":
            for dep in dependencies:
                if not check_dependency(dep):
                    install_dependency(dep)
            print("All dependencies have been installed. You can now run the script.")

if __name__ == "__main__":
    main()