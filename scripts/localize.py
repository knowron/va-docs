import os
root = ".."

replace_pairs = [
    ("KNOWRON", "ASMPT"), 
    ("Knowron", "ASMPT"), 
    ("Assistant", "Virtual Assist App"), 
    ("Assistent", "Virtual Assist App"), 
    ("Control Suite", "Virtual Assist Web")
    ]

exceptions = [""]

def replace(filename):
    # Read in the file
    with open(filename, 'r') as file :
        filedata = file.read()

    # Replace the target string
    for pair in replace_pairs:
        filedata = filedata.replace(pair[0], pair[1])

    # Write the file out again
    with open(filename, 'w') as file:
        file.write(filedata)

def undo_replace(filename):
        # Read in the file
    with open(filename, 'r') as file :
        filedata = file.read()

    # Replace the target string
    for pair in replace_pairs:
        filedata = filedata.replace(pair[1], pair[0])

    # Write the file out again
    with open(filename, 'w') as file:
        file.write(filedata)


if __name__ == "__main__":
    
    for path, subdirs, files in os.walk(root):
        for name in files:
            full_filepath = os.path.join(path, name)
            filename, file_extension = os.path.splitext(full_filepath)
            if file_extension == ".md":
                replace(full_filepath)