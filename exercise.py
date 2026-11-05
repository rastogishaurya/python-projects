import os

def ask_folder():
    count =0
    folder  = input("Enter folder name:").strip().strip('""')
    ext = input("which extension type files to see: ")
    if not ext.startswith("."):
        ext = "." + ext
    if os.path.isdir(folder):
        for filename in os.listdir(folder):

            if filename.lower().endswith(ext.lower()):
                count += 1
                print(filename)
        print(f"found  {count} files")

    else:
        print("folder not found")            

ask_folder()
