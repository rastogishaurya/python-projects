import os
import shutil



CATEGORIES = {
    # Spreadsheets
    ".csv": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".xls": "Spreadsheets",
    # Images
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    # Documents
    ".pdf": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".txt": "Documents",
    # Presentations
    ".pptx": "Presentations",
    ".ppt": "Presentations",
    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    # Code
    ".py": "Code",
    ".java": "Code",
    ".c": "Code",
    ".cpp": "Code",
    ".html": "Code",
    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
}




  
def get_category(filename):
    extension = os.path.splitext(filename)[1].lower()
    return CATEGORIES.get(extension, "Other")

def get_unique_path(path):
    base, ext = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = base + "_" + str(counter) + ext
        counter += 1
    return path
    # print("Final destination:", new_path)  

def organise_folder(folder, dry_run):
    for filename in os.listdir(folder):
        old_path = os.path.join(folder, filename)
 
        if not os.path.isfile(old_path):
            continue
 
        category = get_category(filename)
        target_folder = os.path.join(folder, category)
        new_path = get_unique_path(os.path.join(target_folder, filename))
 
        if dry_run:
            print("Would move", filename, "-->", category)
        else:
            try:
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(old_path, new_path)
                print("Moved", filename, "-->", category)
            except PermissionError:
                print("Permission denied:", filename)
            except OSError as e:
                print("Could not move", filename, ":", e)

def ask_folder():
    while True:
        folder = input("Which folder to organise? ").strip()
        if os.path.isdir(folder):
            return folder
        print("That folder doesn't exist. Try again.")



def main():
    folder = ask_folder()
    answer = input("Preview only (dry run)? y/n: ").lower()
    dry_run = (answer == "y")
    organise_folder(folder, dry_run)
 
 
if __name__ == "__main__":
    main()        
