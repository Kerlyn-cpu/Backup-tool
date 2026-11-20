# Automated Directory Backup Tool

## Description
A Python command-line utility that automates the process of backing up a local directory to a new location. It verifies that the source directory exists before executing the copy process to prevent errors.

## Features
- Takes user input for source and target directories.
- Validates if the source directory actually exists.
- Uses `shutil.copytree` to safely copy all files and sub-directories.

## Technologies Used
- Python 3
- `os` module
- `shutil` module

## How to Run
1. Run the script:
   `python3 Backup_tool.py`
2. Enter the folder you want to back up (e.g., `Documents`).
3. Enter the target location for the backup.
