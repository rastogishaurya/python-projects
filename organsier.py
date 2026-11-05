import os
import shutil

DRY_RUN = False

CATEGORIES = {
    ".csv": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".png": "images",
    ".jpg": "images",
    ".pdf": "documents",
    ".docx": "documents",
    ".txt": "documents",
}

folder = input("which folder to organise?")

for filename in os.listdir(folder):
  old_path = os.path.join(folder,filename)

  if not os.path.isfile(old_path):
    continue

  extension = os.path.splitext(filename)[1].lower()
  target = CATEGORIES.get(extension,"other")



  target_folder = os.path.join(folder,target)
  new_path = os.path.join(target_folder,filename)
  name,ext = os.path.splitext(filename)


  counter  = 1
  while os.path.exists(new_path):
    new_path = os.path.join(target_folder,name+"_"+ str(counter)+ext)
    counter+=1

  print("Final destination:", new_path)  


  if DRY_RUN:
    print("Would move",filename,"-->",target) 
  else:
     try:
        os.makedirs(target_folder, exist_ok=True)
        shutil.move(old_path, new_path)
        print("Moved", filename, "-->",target)
     except PermissionError:
        print("Permission denied:", filename)
     except OSError as e:
          print("Could not move", filename, ":", e)
