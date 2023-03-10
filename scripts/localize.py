import os, shutil
root = ".."

replace_pairs = [
    ("KNOWRON Assistant", "ASMPT Virtual Assist"), 
    ("Native Assistant", "Virtual Assist App"), 
    ("Assistant", "Virtual Assist App"), 
    ("Assistent", "Virtual Assist App"), 
    ("Control Suite", "Virtual Assist Web"),
    ("Knowron", "ASMPT Virtual Assist"),
    ("KNOWRON", "ASMPT Virtual Assist"),

    # Images
    ("imgur.com/EAaxESg", "imgur.com/mL7XYMH"), # Banner image,

    # Links
    ("mailto:arturo@knowron.com", "https://smt.asmpt.com/en/products/software-solutions/virtual-assist"),
    ("https://docs.knowron.com", "https://va-docs.knowron.com"),
    ("https://suite.knowron.com", "https://virtualassist.smt.asmpt.com/"),
    # YML config
    ("site_name: KNOWRON", "site_name: Virtual Assist Docs"),
    ("primary: deep orange", "primary: red"),
    ("accent: indigo", "accent: orange"),
    ("<arturo@knowron.com>", "[us](https://smt.asmpt.com/en/products/software-solutions/virtual-assist)"),
    ]

ignore = [".github", "site", ".git"]

exceptions = [""]

def replace(filename):
    # Read in the file
    with open(filename, 'r') as file :
        filedata = file.read()

    # Replace the target string
    new_filedata = replace_target_string_from_pairs(filedata, replace_pairs)

    # Write the file out again
    with open(filename, 'w') as file:
        file.write(new_filedata)

def replace_target_string_from_pairs(input_string, pairs = replace_pairs):
    for pair in pairs:
        input_string = input_string.replace(pair[0], pair[1])
    return input_string

def undo_replace(filename):
    # Read in the file
    with open(filename, 'r') as file:
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

def localize():
    for path, subdirs, files in os.walk(root):
        for name in files:
            full_filepath = os.path.join(path, name)
            filename, file_extension = os.path.splitext(full_filepath)
            if (file_extension == ".md" or file_extension=="yml") and not should_be_ignored(path):
                print("Processing " +filename + "...")
                replace(full_filepath)
                os.rename(full_filepath, replace_target_string_from_pairs(full_filepath))
    post_process()

def post_process():
    # CNAME
    cname_path = '../docs/CNAME'
    if os.path.isfile(cname_path):
        with open(cname_path, 'w') as file:
            file.writelines("va-docs.knowron.com")

    # Icons
    shutil.copyfile("../docs/icon-asmpt.png", ("../docs/icon.png"))
    shutil.copyfile("../docs/logo-asmpt.png", ("../docs/logo.png"))

    # yml file
    shutil.copyfile("../../docs/mkdocs.yml", "../mkdocs.yml")
    replace("../mkdocs.yml")


if __name__ == "__main__":
    # localize()
    print(replace_target_string_from_pairs("KNOWRON"))
