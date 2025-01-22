# Automated File Backup Program

This Python script is designed to automate the process of backing up a folder to a specified directory on a daily schedule. It uses the `schedule` library to handle the timing of the backup tasks.

## Features
- Automatically copies the contents of a specified folder to a destination folder.
- Creates a new subfolder in the destination folder with the current date as the folder name.
- Avoids overwriting by checking if the folder for the current date already exists.
- Runs daily at a specified time.

## Prerequisites

Ensure you have the following installed:
- Python 3.6 or later
- Required Python libraries:
  - `os`
  - `shutil`
  - `datetime`
  - `time`
  - `schedule`

You can install the `schedule` library using pip:
```bash
pip install schedule
```

## Setup
1. Clone or download this repository to your local machine.
2. Modify the `source_dir` and `destination_dir` variables in the script to match your source and destination folder paths.

```python
source_dir = "C:/Users/amine/OneDrive/Images/Pellicule"
destination_dir = "C:/Users/amine/OneDrive/Documents/Backups"
```

3. Adjust the backup schedule if needed by modifying the time in the following line:

```python
schedule.every().day.at("13:28").do(lambda: copy_folder_to_directory(source_dir, destination_dir))
```

## Usage

Run the script in your Python environment:

```bash
python automated_backup.py
```

The script will continuously run in the background, checking every minute for the scheduled time to perform the backup.

## How It Works

1. **Folder Copy Function**
   - The `copy_folder_to_directory` function creates a subfolder in the destination directory named after the current date and copies the contents of the source folder into it.

2. **Scheduling**
   - The `schedule` library is used to trigger the backup task daily at the specified time.

3. **Infinite Loop**
   - The script enters an infinite loop to constantly check if it's time to run the scheduled task. It uses `time.sleep(60)` to wait for a minute between checks.

## Example Output

When the backup is successful:
```
Successfully copied to: C:/Users/amine/OneDrive/Documents/Backups/2025-01-22
```

If the backup folder already exists:
```
Folder already exists in: C:/Users/amine/OneDrive/Documents/Backups
```

## Customization
- You can customize the source and destination directories and the backup schedule to fit your needs.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
