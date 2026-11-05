
from organiser1 import organise_folder, undo_last

folder = r"C:\Users\rasto\OneDrive\Desktop\pythonprojects\python_for_ai\test_folder"

organise_folder(folder, False)
input("Check the folder in File Explorer, then press Enter to undo...")
undo_last(folder)