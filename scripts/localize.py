import os, shutil
import re
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



    #######################  Documents ################### 

    # Documents page
    ("https://i.imgur.com/Y5GOTyu.png","https://i.imgur.com/QrtEaVR.png"),

    # Documents metadata
    ("https://i.imgur.com/rl3dY4M.png","https://i.imgur.com/vUIttp8.png"),

    # Docs Preview
    ("https://i.imgur.com/h0sXFpE.gif","https://i.imgur.com/HCfry0o.gif"),

    # Docs Delete
    ("https://i.imgur.com/0b8f81V.gif","https://i.imgur.com/stBe7FW.gif"),

    # Documents Share 
    ("https://i.imgur.com/1ns9qVC.png","https://i.imgur.com/HDEov7H.png"),

    # Documents Download 
    ("https://i.imgur.com/dVBtEsD.png","https://i.imgur.com/TYc9Qxv.png"),

    # Documents Title
    ("https://i.imgur.com/m28R6Pj.png","https://i.imgur.com/T792Jhy.png"),
   
    # Tags EN
    ("https://i.imgur.com/AzOobeD.png"," https://i.imgur.com/0qLxYwh.png"),
    # Tags DE
    ("https://i.imgur.com/2wkw8Ji.png"," https://i.imgur.com/0qLxYwh.png"),

    # Add Tags EN
    ("https://i.imgur.com/riFMvsH.jpg","https://i.imgur.com/DRUKkNT.jpg"),
     # Add Tags DE
    ("https://i.imgur.com/vpODjpY.png","https://i.imgur.com/DRUKkNT.jpg"),
  
    #######################  Search ################### 


    # Search Bar
    ("https://i.imgur.com/depHqSZ.png","https://i.imgur.com/ceW9eZG.png"),
   

    # Result List EN
    ("https://i.imgur.com/JaUJWFH.png","https://i.imgur.com/kzz0K42.png"),
    # Result List DE
    ("https://i.imgur.com/s8gV87t.png","https://i.imgur.com/kzz0K42.png"),

    # Translated Results EN
    ("https://i.imgur.com/W6nVTdU.png","https://i.imgur.com/F48xlTa.png"),

    # Results not helpful EN
    ("https://i.imgur.com/UFzgbTV.png","https://i.imgur.com/mlk423q.jpg"),
    # Results not helpful
    ("https://i.imgur.com/icwXGkg.png","https://i.imgur.com/mlk423q.jpg"),

    # Feedback Box EN
    ("https://i.imgur.com/XDwSOdu.png","https://i.imgur.com/V1t3eeb.png"),
    # Feedback Box DE
    ("https://i.imgur.com/q52nK3B.png","https://i.imgur.com/V1t3eeb.png"),

    # Filters: Tags EN
    ("https://i.imgur.com/KjkplBs.png","https://i.imgur.com/BsIkF62.png"),
     # Filters: Tags DE
    ("https://i.imgur.com/KjkplBs.png","https://i.imgur.com/BsIkF62.png"),

    # Filters: Languages EN
    ("https://i.imgur.com/AyujrBQ.png","https://i.imgur.com/3sEgfAg.png"),
    # Filters: Languages DE
    ("https://i.imgur.com/cKzeomC.png","https://i.imgur.com/3sEgfAg.png"),

    # Filters: Time
    ("https://i.imgur.com/kJlRr1E.png","https://i.imgur.com/xCrBnEh.png"),
    # Filters: Time
    ("https://i.imgur.com/H0ImR2T.png","https://i.imgur.com/xCrBnEh.png"),


    ######################  Articles ################### 

    # Create Article Gif
    ("https://i.imgur.com/Q4M8Ufs.gif","https://i.imgur.com/1HSh18N.gif"),

    # Create Article Template
    ("https://i.imgur.com/Q4M8Ufs.gif","https://i.imgur.com/48Q1x5C.gif"),

    # Create Article + add image
    ("https://i.imgur.com/NqV0zII.gif","https://i.imgur.com/xQKWR3e.gif"),
    
    # Articles preview 

    ("https://i.imgur.com/wwKD05L.gif","https://i.imgur.com/TW6MyCM.gif"),

    # Edit Article
    ("https://i.imgur.com/QiQcfjQ.png","https://i.imgur.com/5ZTiBqo.png"),

    # Delete Article
    ("https://i.imgur.com/0qmI1d2.png","https://i.imgur.com/8fW8IPR.png"),

    # Articles Table
    ("https://i.imgur.com/Djfon62.png","https://i.imgur.com/bdKqUUW.png"),

    # Share Articles
    ("https://i.imgur.com/AVBDSLs.png","https://i.imgur.com/9jIfUot.png"),

    ######################  Admin Panel ################### 

    # Upload Privacy Policy EN
    ("https://i.imgur.com/4Auw9bG.gif","https://i.imgur.com/H02gNPV.gif"),
    # Upload Privacy Policy DE
    ("https://i.imgur.com/EZyvUYZ.gif","https://i.imgur.com/H02gNPV.gif"),

    # User management EN
    ("https://i.imgur.com/4Auw9bG.gif",""),
     # User management EN
    ("https://i.imgur.com/ZT9Q1u1.gif",""),



    #################### Logbook ######################

    # 
    ("https://i.imgur.com/BKE7IV9.gi","https://i.imgur.com/pAmAHTF.gif"),
    # 
    ("https://i.imgur.com/3NQ9e9X.gif","https://i.imgur.com/PiIpt1F.gif"),
    #
    ("https://i.imgur.com/NETD64k.gif","https://i.imgur.com/kHjpJQo.gif"),

    
    #################### Machine Inventory ######################

    # Intro image
    ("https://i.imgur.com/rTruWjI.gif", "https://i.imgur.com/9SFdtZC.gif"),
    # Adding machines
    ("https://i.imgur.com/7F9L59T.gif", "https://i.imgur.com/6D9GhLI.gif"),
    # QR codes for the machine
    ("https://i.imgur.com/s9BOpW8.gif", "https://i.imgur.com/PYTYa1F.gif"),


    ################### Tutorials ################### 

    # Step 1 EN
    ("https://i.imgur.com/8z30N8T.gif","https://i.imgur.com/CNlZKs7.gif"),
    # Step 1 DE
    ("https://i.imgur.com/lj6pLuA.gif","https://i.imgur.com/CNlZKs7.gif"),

    
    # Step 2 EN
    ("https://i.imgur.com/Et7I6sR.gif","https://i.imgur.com/tUWAEi5.gif"),
    # Step 2 DE
    ("https://i.imgur.com/7dhtHdB.gif","https://i.imgur.com/tUWAEi5.gif"),


    # Step 3 EN
    ("https://i.imgur.com/6DLmhxW.gif","https://i.imgur.com/sKlSbTO.gif"),
    # Step 3 DE
    ("https://i.imgur.com/Pw0bbz0.gif","https://i.imgur.com/sKlSbTO.gif"),


    # Step 4 EN
    ("https://i.imgur.com/7WBpvpM.gif","https://i.imgur.com/jkm8nCe.gif"),
    # Step 4 DE
    ("https://i.imgur.com/1ah1Wud.gif","https://i.imgur.com/jkm8nCe.gif"),

    # Step 5 EN
    ("https://i.imgur.com/Uccurnr.gif","https://i.imgur.com/u973bwk.gif"),
    # Step 5 DE
    ("https://i.imgur.com/dYfNNNS.gif","https://i.imgur.com/u973bwk.gif"),


    

    ###########################  Native Assitant ################### 

    ########### Support screen ###########

    # E-mail Assitance
    ("https://i.imgur.com/3QiM3Bi.gif","https://i.imgur.com/vM0OIZG.gif"),
    # Connect with reginal support 
    ("https://i.imgur.com/UhnaGSk.gif","https://i.imgur.com/ryXRHA1.gif"),
    
    ########### Documents ###########

    # Filters EN
    ("https://i.imgur.com/i1cBJeH.gif","https://i.imgur.com/wM4LMgJ.gif"),
    # Info button DE
    ("https://i.imgur.com/i1cBJeH.gif","https://i.imgur.com/wM4LMgJ.gif"),

    # Info button EN
    ("https://i.imgur.com/x3sc8CF.gif","https://i.imgur.com/pWpga0K.gif"),
     # Info button DE
    ("https://i.imgur.com/x3sc8CF.gif","https://i.imgur.com/pWpga0K.gif"),


    ############# Push notifications ###############

    # Give permissions EN
    ("https://i.imgur.com/47aAXlh.jpg","https://i.imgur.com/mjbLm7O.jpg"),
    
    ############Give permissions EN#############
    ("https://i.imgur.com/47aAXlh.jpg","https://i.imgur.com/mjbLm7O.jpg"),
    
    # See notification EN 
    ("https://i.imgur.com/uLsA1EO.gif","https://i.imgur.com/ppbpLgc.gif"),
     # See notification DE
    ("https://i.imgur.com/uLsA1EO.gif","https://i.imgur.com/ppbpLgc.gif"),


   ############ Machine Details ###############

   # EN
    ("https://i.imgur.com/KimphwK.gif","https://i.imgur.com/uSm7zhg.gif"),
   # DE
    ("https://i.imgur.com/KimphwK.gif","https://i.imgur.com/uSm7zhg.gif"),



   ############ AI Answewrs ###############

   # Your query was asked too broadly and no answer can be formulated from the top results
    ("https://i.imgur.com/P5dffZP.png","https://i.imgur.com/nBP5YAx.png"),
    ("https://i.imgur.com/ng1mKcs.png","https://i.imgur.com/UCXLTSH.png"),

   # The information you are looking for is not found in the documents provided
    ("https://i.imgur.com/tF97eUG.png","https://i.imgur.com/sWnOeQ5.png"),

    # The documentation might be using a different name for the topic that you are looking for

    ("https://i.imgur.com/sxsfxsH.png","https://i.imgur.com/tMWmrTX.png"),
    ("https://i.imgur.com/hjy43O3.png","https://i.imgur.com/L9Tq3B3.png"),

    #You were looking for something that is in an image

    ("https://i.imgur.com/A5UQTgy.png","https://i.imgur.com/Vn18LIp.png"),

    ############## Insights Dashboard ##########

    ("https://i.imgur.com/ro4PDcx.png", "https://i.imgur.com/Vo6AOmh.png"),
    ("https://i.imgur.com/m48FwjW.gif", "https://i.imgur.com/H9UPPOK.gif"),
    ("https://i.imgur.com/jKsjvL2.gif", "https://i.imgur.com/ZpPo2JN.gif"),
    ("https://i.imgur.com/bgsj6OF.png", "https://i.imgur.com/YpC7INA.png"),
    ("https://i.imgur.com/MxkHupO.png", "https://i.imgur.com/KTLQrHi.png"),
    ("https://i.imgur.com/xPuCYPj.gif", "https://i.imgur.com/BtWiY46.gif"),
    ("https://i.imgur.com/R3ZQZPM.png", "https://i.imgur.com/JRhv6o5.png"),
    ("https://i.imgur.com/W25B2OT.gif", "https://i.imgur.com/W4tb9c4.gif"),
    ("https://i.imgur.com/Dumfa1e.gif", "https://i.imgur.com/ajgErFN.gif"),
    # ("xyz", "abc"),
    # ("xyz", "abc"),

    ############## Link Sharing ################

     ("https://i.imgur.com/wwHhhe3.gif","https://i.imgur.com/cHpbe5G.gif"),
     ("https://i.imgur.com/5Z71FC7.gif","https://i.imgur.com/6YBUY6z.gif"),
     ("https://i.imgur.com/8x1JXJP.png","https://i.imgur.com/XhEc8pN.jpg"),
     ("https://i.imgur.com/5cCT2eY.png","https://i.imgur.com/ucvZ0bq.png"),
     
    ############### Insights ###########
    ("https://i.imgur.com/ro4PDcx.png","https://i.imgur.com/Vo6AOmh.png"),
    ("https://i.imgur.com/m48FwjW.gif","https://i.imgur.com/LbSI8kV.gif"),
    ("https://i.imgur.com/jKsjvL2.gif","https://i.imgur.com/ZpPo2JN.gif"),
    # History 
    ("https://i.imgur.com/Xxu7oHp.png",""),


    # Links

    ("mailto:arturo@knowron.com", "https://smt.asmpt.com/en/products/software-solutions/virtual-assist"),
    ("https://docs.knowron.com", "https://docs.virtualassist.smt.asmpt.com"),
    ("https://suite.knowron.com", "https://virtualassist.smt.asmpt.com/"),
    ("https://www.knowron.com", "https://smt.asmpt.com/en/products/software-solutions/virtual-assist"),
    ("suite.knowron.com", "virtualassist.smt.asmpt.com"),
    ("<arturo@knowron.com>", "[us](https://smt.asmpt.com/en/products/software-solutions/virtual-assist)"),
    ("ask@knowron.com", "asm-support.df@asmpt.com"),
    ("arturo@knowron.com", "asm-support.df@asmpt.com"),
    
    ("https://play.google.com/store/apps/details?id=com.knowron.assistant.knowron", "https://play.google.com/store/apps/details?id=com.knowron.assistant.asmassistant"),
    ("https://apps.apple.com/en-us/app/knowron-assistant/id1585382448", "https://apps.apple.com/eg/app/asmpt-virtual-assist/id1614625842"),
    ("https://apps.apple.com/at/app/knowron-assistant/id1585382448", "https://apps.apple.com/eg/app/asmpt-virtual-assist/id1614625842"),


    # YML config
    ("site_name: KNOWRON", "site_name: Virtual Assist Docs"),
    ("primary: deep orange", "primary: red"),
    ("accent: indigo", "accent: red"),
    ("FA6E3F", "ac3229"),
    ("      - \"Features/troubleshooting_na.md\"", ""),
    ("      - \"Features/machineinventory.md\"", ""),
    ("      - \"Features/partsinventory.md\"", ""),
    ("      - \"Features/charts.md\"", ""),
    ("      - \"Admin Documentation/subtenancy.md\"", ""),
    ("      - \"Features/inventory_na.md\"", ""),
    
    ]

ignore = [".github", "site", ".git"]

exceptions = [""]

def remove_comments(input_string):
    pattern = r'\[comment\]: KNOWRON-ONLY-START[\s\S]*?\[comment\]: KNOWRON-ONLY-END\n?'

    result = re.sub(pattern, '', input_string)
    return result


def replace(filename):
    # Read in the file
    with open(filename, 'r') as file :
        filedata = file.read()

    # Replace the target string
    new_filedata = remove_comments(filedata)
    new_filedata = replace_target_string_from_pairs(new_filedata, replace_pairs)

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
    print("Post Processing...")
    # CNAME
    cname_path = '../docs/CNAME'
    print("Creating CNAME file...")
    if os.path.isfile(cname_path):
        with open(cname_path, 'w') as file:
            file.writelines("docs.virtualassist.smt.asmpt.com")

    print("Copying images...")
    # Icons
    shutil.copyfile("../docs/icon-asmpt.png", ("../docs/icon.png"))
    shutil.copyfile("../docs/logo-asmpt.png", ("../docs/logo.png"))

    print("Copying yml file...")
    # yml file
    shutil.copyfile("../../knowron-docs/mkdocs.yml", "../mkdocs.yml")
    replace("../mkdocs.yml")


if __name__ == "__main__":
    # localize()
    print(replace_target_string_from_pairs("KNOWRON"))
