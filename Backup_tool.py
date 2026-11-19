
import os
import shutil
import datetime


def Backup_Tool():
    home_path = os.path.expanduser('~')
    source_name = input("Enter the folder to back up 🤨: ")
    source_name_lower = source_name.lower()
    allowed = ['Documents','Downloads','Desktop','Pictures','Videos','Music',]
    walk = os.walk(home_path)
    for root,folders,files in walk:
        if root == home_path:
            folders[:]=[f for f in folders if f in allowed]
        lower_case_folders = [f.lower() for f in folders]    
        if source_name_lower in lower_case_folders:
                    match_index = lower_case_folders.index(source_name_lower)
                    exact_folder_name = folders[match_index]
                    real_folder_path = os.path.join(root,exact_folder_name)
                    current_date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                    unique_backup_name = (f"{source_name}_{current_date}")
                    Backup_folder = os.path.join(home_path,'Backup files')
                    os.makedirs(Backup_folder,exist_ok=True)
                    target_location = os.path.join(Backup_folder,unique_backup_name)
                    shutil.copytree(real_folder_path,target_location) 
                    print("✅Backup complete🎉")
                    print(f"📁Backup named {unique_backup_name}")
                    break              
    else:
                   print("Directory not found😆")
                   print("Please input the correct folder 🙂") 
                               
Backup_Tool()  