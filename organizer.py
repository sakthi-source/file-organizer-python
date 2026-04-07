import os
import shutil

folder_path = "test_folder"

files = os.listdir(folder_path)

for file in files:
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        if file.endswith(".jpg") or file.endswith(".png"):
            os.makedirs(folder_path + "/Images", exist_ok=True)
            shutil.move(file_path, folder_path + "/Images/" + file)

        elif file.endswith(".pdf") or file.endswith(".txt"):
            os.makedirs(folder_path + "/Documents", exist_ok=True)
            shutil.move(file_path, folder_path + "/Documents/" + file)

        elif file.endswith(".mp3"):
            os.makedirs(folder_path + "/Music", exist_ok=True)
            shutil.move(file_path, folder_path + "/Music/" + file)

        elif file.endswith(".mp4"):
            os.makedirs(folder_path + "/videos",exist_ok=true)
            shutil.move(file_path,folder_path + "/videos/" + file)
            
print("Files organized successfully")
