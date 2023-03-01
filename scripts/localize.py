import os
root = ".."

replace_pairs = [
    ("KNOWRON", "ASMPT"), 
    ("Knowron", "ASMPT"), 
    ("Assistant", "Virtual Assist App"), 
    ("Assistent", "Virtual Assist App"), 
    ("Control Suite", "Virtual Assist Web")
    ]

ignore = [".github", "site", ".git"]

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


def should_be_ignored(filepath):
    path_components = os.path.normpath(filepath).split(os.path.sep)
    for element_to_be_ignored in ignore:
        if element_to_be_ignored in path_components:
            return True
    return False


if __name__ == "__main__":
    
    for path, subdirs, files in os.walk(root):
        for name in files:
            full_filepath = os.path.join(path, name)
            filename, file_extension = os.path.splitext(full_filepath)
            if file_extension == ".md" and not should_be_ignored(path):
                print("Processing " +filename + "...")
                replace(full_filepath)