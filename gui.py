import tkinter as tk
from tkinter import filedialog
from parser import parse_folder

def launch_gui():
    def select_folder():
        folder_path = filedialog.askdirectory()
        if folder_path:
            print("Selected Folder: ", folder_path)
            path_label.config(text=f"📁 {folder_path}")

            summary =  parse_folder(folder_path)

            formatted = (
                f"📁 Folders: {summary['folders']}\n"
                f"📄 Files: {summary['files']}\n"
                f"💾 Total Size: {summary['size_formatted']} ({summary['size_bytes']} bytes) "
            )
            formatted+="\n\n📦 File Types: \n"
            for ext, count in summary["file_types"].items():
                display_ext = ext if ext else "[no ext]"
                formatted+= f" {display_ext}: {count}\n"

            result_label.config(text=formatted)

        else:
            print("No folder selected.")

    root = tk.Tk()
    root.title("Folder Summary Parser")
    root.geometry("500x250")

    select_button = tk.Button(root, text="Select Folder", command=select_folder)
    select_button.pack(pady=20)

    path_label = tk.Label(root, text="No folder selected yet.")
    path_label.pack()

    result_label = tk.Label(root, text="", justify="left")
    result_label.pack(pady=10)

    root.mainloop()
