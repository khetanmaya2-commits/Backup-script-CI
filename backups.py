import shutil
import datetime
import os

def backup_files(source,destination):
    today = datetime.datetime.today().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file_name= os.path.join(destination, f"backup_{today}")
    shutil.make_archive(backup_file_name,'gztar',source)

    print("Backup Created Successfully")

source="sample_data"
destination= "backup"

backup_files(source,destination)