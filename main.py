import os
import shutil
import datetime
import time
import schedule

source_dir = "C:/Users/amine/OneDrive/Images/Pellicule"
destination_dir = "C:/Users/amine/OneDrive/Documents/Backups"

def copy_folder_to_directory(src, dest):
  today = datetime.date.today()
  dest_dir = os.path.join(dest, str(today))

  try:
    shutil.copytree(src, dest_dir)
    print(f"Successfully copied to: {dest_dir}")
  except FileExistsError:
    print(f"Folder already exists in: {dest}")

schedule.every().day.at("13:28").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
  schedule.run_pending()
  time.sleep(60)