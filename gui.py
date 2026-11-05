import os
import tkinter as tk
from tkinter import filedialog,messagebox
from organiser1 import organise_folder, print_summary, undo_last

def browse():
    folder   = filedialog.askdirectory()
    if folder:
        folder_var.set(folder)

def log_message(text):
    output_box.insert(tk.END,text+"\n")
    output_box.see(tk.END)        


def run():
    folder = folder_var.get()
    if not os.path.isdir(folder):
        messagebox.showerror("Error","Please choose a valid folder.")
        return

    
    if not preview_var.get():                                                    
        if not messagebox.askyesno("Confirm", "This will move files. Continue?"):  
            return   
        
    output_box.delete("1.0",tk.END)
    try:
       counts = organise_folder(folder, preview_var.get(), log_message)
       print_summary(counts, log_message)
    except Exception as e:
        messagebox.showerror("Error",f"Something went wrong:\n{e}")  


def undo():
    folder = folder_var.get()
    if not os.path.isdir(folder):
        messagebox.showerror("Error", "Please choose a valid folder.")
        return

    if not messagebox.askyesno("Confirm", "Undo the last organise in this folder?"):
        return

    output_box.delete("1.0", tk.END)
    try:
        undo_last(folder, log_message)
    except Exception as e:
        messagebox.showerror("Error", f"Undo failed:\n{e}")         

root = tk.Tk()
root.title("File Organiser")
root.geometry("500x470")


folder_var = tk.StringVar()

tk.Label(root, text = "Folder to organise:").pack(pady=(15,5))
tk.Entry(root,textvariable = folder_var,width = 60).pack()
tk.Button(root,text = "Browse",command = browse).pack(pady=10)


preview_var = tk.BooleanVar(value=True)
tk.Checkbutton(root,text = "Preview only (dry run)",variable=preview_var).pack()
tk.Button(root,text = "Organise",command=run).pack(pady=10)

tk.Button(root, text="Undo last organise", command=undo).pack(pady=(0, 10))

output_box = tk.Text(root, height=10, width=65)
output_box.pack(padx=10, pady=(0, 10))

root.mainloop()