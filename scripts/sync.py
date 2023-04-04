from localize import localize
import shutil
import os

def sync():
    original_path = "../../knowron-docs/docs"
    destination_path ="../docs"
    if os.path.isdir(original_path) and os.path.isdir(destination_path):
        shutil.copytree(original_path, destination_path, dirs_exist_ok=True)
    
if __name__ == "__main__":
    sync()
    localize()