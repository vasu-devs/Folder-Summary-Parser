import os
from utils import format_size
from collections import defaultdict

def parse_folder(path):
    total_files=0
    total_folders=0
    total_size=0
    file_types= defaultdict(int)

    for root, dirs, files in os.walk(path):

        total_folders+=len(dirs)
        total_files += len(files)

        for file in files:
            try:
                file_path = os.path.join(root,file)
                total_size+= os.path.getsize(file_path)
                ext = os.path.splitext(file)[1].lower()
                file_types[ext]+=1
            except Exception as e:
                print("⚠️ Skipped file due to error: {file_path} - {e}")
    
    return {
        "files" : total_files,
        "folders" : total_folders,
        "size_bytes": total_size,
        "size_formatted": format_size(total_size),
        "file_types": dict(file_types)
    }