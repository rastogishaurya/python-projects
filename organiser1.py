import os
import shutil
import json

LOG_NAME= "move_log.json"



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

def save_log(folder, moves):
    with open (os.path.join(folder,LOG_NAME),"w") as f:
        json.dump(moves,f)  

def organise_folder(folder, dry_run,log = print):
    counts={}
    moves = []
    for filename in os.listdir(folder):
        old_path = os.path.join(folder, filename)
 
        if not os.path.isfile(old_path) or  filename == LOG_NAME:
            continue
 
        category = get_category(filename)
        target_folder = os.path.join(folder, category)
        new_path = get_unique_path(os.path.join(target_folder, filename))
 
        if dry_run:
            log(f"Would move  {filename}  --> {category}")
            counts[category]=counts.get(category,0)+1
        else:
            try:
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(old_path, new_path)
                moves.append([old_path,new_path])
                counts[category]= counts.get(category,0)+1
                log(f"Moved   {filename} -->  {category}")
            except PermissionError:
                log("Permission denied: " +  filename)
            except OSError as e:
                    log(f"Could not move  {filename} : {e}" )
    if moves:
        save_log(folder,moves)
    return counts    


def undo_last(folder, log=print):
    log_path = os.path.join(folder, LOG_NAME)
    if not os.path.exists(log_path):
        log("Nothing to undo.")
        return

    with open(log_path) as f:
        moves = json.load(f)

    restored = 0
    for old_path, new_path in reversed(moves):
        if not os.path.exists(new_path):
            log(f"Skipped (file missing): {new_path}")
            continue
        try:
            shutil.move(new_path, get_unique_path(old_path))
            log(f"Restored {os.path.basename(old_path)}")
            restored += 1
        except OSError as e:
            log(f"Could not restore {new_path}: {e}")

    for category in set(CATEGORIES.values()) | {"Other"}:
        category_path = os.path.join(folder, category)
        if not os.path.isdir(category_path):
            continue
        try:        
            os.rmdir(category_path)
        except OSError as e:
            log(f"Could not remove empty folder {category}: {e}")
            

    os.remove(log_path)
    log(f"Undo complete: {restored} file(s) restored.")

def print_summary(counts,log=print):
    if not counts:
        log("No files found to organise.")
        return
    total =sum(counts.values())
    log("")
    log(f"--- Summary: {total} file(s) ---")
    for category, number in sorted(counts.items()):
        log(f"{category}: {number}")


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
