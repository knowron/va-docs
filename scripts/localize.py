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
    ("what-is-knowron", "what-is-virtual-assist"),

    # Misc text
    ("Epsilon Series", "SIPLACE SX Series"),
    ("mailto:ali@knowron.com?subject=Request for Access&body=Hi,%0D%0A%0D%0A Ich habe keinen Zugriff auf dem System. Schalten Sie mich bitte frei. %0D%0A%0D%0ADanke!", "https://smt.asmpt.com/en/products/software-solutions/virtual-assist"),
    ("mailto:ali@knowron.com?subject=Request for Access&body=Hi,%0D%0A%0D%0AI am unable to access the system. Please provide support.%0D%0A%0D%0AThank you!", "https://smt.asmpt.com/en/products/software-solutions/virtual-assist"),

    # Images
    ("imgur.com/EAaxESg", "imgur.com/mL7XYMH"), # Banner image,
    # QR code Android
    ("https://i.imgur.com/OpA9C58.png", "https://i.imgur.com/nBCQpRk.png"),
    # QR code iOS
    ("https://i.imgur.com/hntAI1x.png", "https://i.imgur.com/iB8uRxb.png"),
    # Where to find your password
    ("https://i.imgur.com/gXh9xJt.png", "https://i.imgur.com/QKwIRJ3.png"),
    # Log in screen native assistant
    ("https://i.imgur.com/FPz6Zsw.gif","https://i.imgur.com/BLv8UFT.gif"),
    # Select a product line
    ("https://i.imgur.com/FNQueGy.png", "https://i.imgur.com/GMsrFUC.png"),
    # Scan a QR code
    ("https://i.imgur.com/pocHR5l.png", "https://i.imgur.com/Yif9Xoc.png"),
    # Type in a question
    ("https://i.imgur.com/1G2skdh.gif", "https://i.imgur.com/XUkQLiO.gif"),
    ("What is PLA", "What is the torque for a CPP head"),
    # Use the search screen
    ("https://i.imgur.com/X4GKmM7.gif", "https://i.imgur.com/HOBy2VG.gif"),
    ("Bauplatte Lebensdauer", "DP drive CP 20 P2"),
    ("printer humidity", "DP drive CP 20 P2"),
    ("In what humidity can the printer be used?", "How do I replace the DP drive on a CP 20 P2?"),
    ("Wie lange ist die Lebensdauer der Bauplatte?", "How do I replace the DP drive on a CP 20 P2?"),
    # Feedback text
    ("https://i.imgur.com/9rXj4j9.gif", "https://i.imgur.com/nTcK9ed.gif"),
    # Feedback upvote
    ("https://i.imgur.com/puislfv.gif", "https://i.imgur.com/ycSgnra.gif"),
    # Log in screen
    ("https://i.imgur.com/h3OoieE.png", "https://i.imgur.com/5I1HipS.png"),
    # Select a product line
    ("https://i.imgur.com/TfkKWZ3.gif", "https://i.imgur.com/wJy7OjB.gif"),
    # Upvote
    ("https://imgur.com/t2tkFxe.gif","https://i.imgur.com/6k68K3K.gif"),
    # Text feedback CS
    ("https://i.imgur.com/i44sdhx.gif","https://i.imgur.com/6Nzj6Kc.gif"),
    # Ask a question CS EN
    ("https://i.imgur.com/a1M9jUN.gif","https://i.imgur.com/CeziNWT.gif"),
    # Ask a question CS DE
    ("https://i.imgur.com/HI3nVYq.gif","https://i.imgur.com/CeziNWT.gif"),
    #### Documents
    # Documents metadata
    ("https://i.imgur.com/YwcPATo.png","https://i.imgur.com/0sLjcSS.png"),
    # Tags
    ("https://i.imgur.com/AzOobeD.png"," https://i.imgur.com/0qLxYwh.png"),
    # Add Tags
    ("https://i.imgur.com/riFMvsH.jpg","https://i.imgur.com/DRUKkNT.jpg"),
  
    #### Search 
    # Search Bar 
    ("https://i.imgur.com/2LytyUp.png","https://i.imgur.com/OOZAis6.png"),
    # Result List
    ("https://i.imgur.com/JaUJWFH.png","https://i.imgur.com/kzz0K42.png"),
    # Translated Results
    ("https://i.imgur.com/SpsQqvY.png","https://i.imgur.com/9cot8He.png"),
    # Verified Result
    ("https://i.imgur.com/ox2ah0e.png","https://i.imgur.com/nSmpzuN.png"),
    # Extracted Result
    ("https://i.imgur.com/GEniWOM.png","https://i.imgur.com/tmxJAt8.png"),
    # Extracted Result bad example
    ("https://i.imgur.com/7x0FpbV.png","https://i.imgur.com/MwO9gOF.png"),
    # Results not helpful
    ("https://i.imgur.com/UFzgbTV.png","https://i.imgur.com/mlk423q.jpg"),
    # Feedback Box
    ("https://i.imgur.com/XDwSOdu.png","https://i.imgur.com/V1t3eeb.png"),



    # Links
    ("mailto:arturo@knowron.com", "https://smt.asmpt.com/en/products/software-solutions/virtual-assist"),
    ("https://docs.knowron.com", "https://docs.virtualassist.smt.asmpt.com"),
    ("https://suite.knowron.com", "https://virtualassist.smt.asmpt.com/"),
    ("https://www.knowron.com", "https://smt.asmpt.com/en/products/software-solutions/virtual-assist"),
    ("suite.knowron.com", "virtualassist.smt.asmpt.com"),
    ("<arturo@knowron.com>", "[us](https://smt.asmpt.com/en/products/software-solutions/virtual-assist)"),

    ("https://play.google.com/store/apps/details?id=com.knowron.assistant.knowron", "https://play.google.com/store/apps/details?id=com.knowron.assistant.asmassistant"),
    ("https://apps.apple.com/en-us/app/knowron-assistant/id1585382448", "https://apps.apple.com/eg/app/asmpt-virtual-assist/id1614625842"),
    ("https://apps.apple.com/at/app/knowron-assistant/id1585382448", "https://apps.apple.com/eg/app/asmpt-virtual-assist/id1614625842"),

    # YML config
    ("site_name: KNOWRON", "site_name: Virtual Assist Docs"),
    ("primary: deep orange", "primary: red"),
    ("accent: indigo", "accent: orange"),
    
    
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
            file.writelines("docs.virtualassist.smt.asmpt.com")

    # Icons
    shutil.copyfile("../docs/icon-asmpt.png", ("../docs/icon.png"))
    shutil.copyfile("../docs/logo-asmpt.png", ("../docs/logo.png"))

    # yml file
    shutil.copyfile("../../docs/mkdocs.yml", "../mkdocs.yml")
    replace("../mkdocs.yml")


if __name__ == "__main__":
    # localize()
    print(replace_target_string_from_pairs("KNOWRON"))
