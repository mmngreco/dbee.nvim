#!/usr/bin/env python3
import sys
from subprocess import check_call

print("Installing dbee.nvi dependencies...")

def main():

    cmd = [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]

    try:
        process = check_call(cmd)
    except Exception as e:
        print("Installation failed!")
        raise e

    print("Done!")


if __name__ == "__main__":
    main()
