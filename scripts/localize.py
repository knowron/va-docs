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
    ("The tool data is stored entirely within the EU (Germany). Documents can be delivered through a Content Delivery Network (CDN) to speed up loading. Only you can access your data (client-level).",
     "The tool data is stored entirely within the EU (Germany). Documents can be delivered through a Content Delivery Network (CDN) to speed up loading. Only you can access your data (client-level) and content. This is also true when creating new product lines with products not manufactured by ASMPT."),
     ("Der Tool-Daten werden vollständig innerhalb der EU (Deutschland) gespeichert. Dokumente können über ein Content Delivery Network (CDN) zur Beschleunigung des Ladens bereitgestellt werden. Nur Sie können auf Ihre Daten zugreifen (auf Kundenebene).",
      "Die Tool-Daten werden vollständig innerhalb der EU (Deutschland) gespeichert. Dokumente können über ein Content Delivery Network (CDN) zur Beschleunigung des Ladens bereitgestellt werden. Nur Sie können auf Ihre Daten (auf Kundenebene) und Inhalte zugreifen. Dies gilt auch, wenn neue Produktlinien mit Produkten erstellt werden, die nicht von ASMPT hergestellt werden."),

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
    ("https://i.imgur.com/HMIItzO.png", "https://i.imgur.com/Jo1FQ1D.png"),
    # Results not helpful
    ("https://i.imgur.com/nImrevY.png","https://i.imgur.com/FRdYNgK.png"),
    ("https://i.imgur.com/jiemEwq.png","https://i.imgur.com/dAcToeD.png"),
    ## Downvoting the Generative Answer
    ("https://i.imgur.com/eGD8ZVd.png","https://i.imgur.com/M3FruL3.png"),
    # Ask a question
    ("https://i.imgur.com/depHqSZ.png","https://i.imgur.com/DxAwOmD.png"),
   



    #######################  Documents ###################################
    #####################################################################

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
  
    #######################  Search ##################################### 
    #####################################################################
    ## Ask Question
    ("https://i.imgur.com/depHqSZ.png","https://i.imgur.com/DxAwOmD.png"),

    ## Translation
    ("https://i.imgur.com/W6nVTdU.png","https://i.imgur.com/YegCmA4.png"),

    ## Language Filter
    ("https://i.imgur.com/XP1Rjzt.png","https://i.imgur.com/6IlcwDO.png"),

    ## Time Filter
    ("https://i.imgur.com/2O0mNRe.png","https://i.imgur.com/gkspfv3.png"),

    ## Tags filter

    ("https://i.imgur.com/2EeYDkB.png",""),

    ## Feedback: Results not helpful Part 1

    ("https://i.imgur.com/nImrevY.png","https://i.imgur.com/FRdYNgK.png"),

     ## Feedback: Results not helpful Part 2

    ("https://i.imgur.com/dAcToeD.png","https://i.imgur.com/jiemEwq.png"),

     ## Feedback: Downvote

    ("https://i.imgur.com/eGD8ZVd.png","https://i.imgur.com/M3FruL3.png"),

    ######################  Articles ###################################
    #####################################################################


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

    ######################  Admin Panel #################################
    #####################################################################

    # Upload Privacy Policy EN
    ("https://i.imgur.com/4Auw9bG.gif","https://i.imgur.com/H02gNPV.gif"),
    # Upload Privacy Policy DE
    ("https://i.imgur.com/EZyvUYZ.gif","https://i.imgur.com/H02gNPV.gif"),

    # User management 
    ("https://i.imgur.com/4Auw9bG.gif","https://i.imgur.com/S5x6z0W.png"),
    
    # Add new user
    ("https://i.imgur.com/tBPOMaZ.gif","https://i.imgur.com/mYdRwZq.gif"),


    #################### Logbook ######################

    # 
    ("https://i.imgur.com/BKE7IV9.gi","https://i.imgur.com/pAmAHTF.gif"),
    # 
    ("https://i.imgur.com/3NQ9e9X.gif","https://i.imgur.com/PiIpt1F.gif"),
    #
    ("https://i.imgur.com/NETD64k.gif","https://i.imgur.com/kHjpJQo.gif"),

    ("https://i.imgur.com/T5EOnQU.mp4", "https://i.imgur.com/RIytQBk.mp4",
     ),
     ("https://i.imgur.com/i8QIb6W.gif", "https://i.imgur.com/NOAHSdM.gif"),
     ("https://i.imgur.com/bKFk3ht.gif", "https://i.imgur.com/VIWwq3D.gif")

    
    #################### Machine Inventory ######################

    # Intro image
    ("https://i.imgur.com/rTruWjI.gif", "https://i.imgur.com/9SFdtZC.gif"),
    # Adding machines
    ("https://i.imgur.com/7F9L59T.gif", "https://i.imgur.com/6D9GhLI.gif"),
    # QR codes for the machine
    ("https://i.imgur.com/s9BOpW8.gif", "https://i.imgur.com/PYTYa1F.gif"),


    ################### Tutorials ######################################### 
    #####################################################################

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

    ## Edit Turorials
    ("https://i.imgur.com/KOwE5Px.gif","https://i.imgur.com/eED75Nx.gif"),



    ############### Insights ###########
    ("https://i.imgur.com/ro4PDcx.png","https://i.imgur.com/Vo6AOmh.png"),
    ("https://i.imgur.com/m48FwjW.gif","https://i.imgur.com/LbSI8kV.gif"),
    ("https://i.imgur.com/jKsjvL2.gif","https://i.imgur.com/ZpPo2JN.gif"),
    ## Feedback
    ("https://i.imgur.com/IAJ3PDe.png","https://i.imgur.com/GsuoKLV.png"),
    # History 
    ("https://i.imgur.com/Xxu7oHp.png","https://i.imgur.com/oLF0mjr.png"),
    ## Top Unasnwered questions
    ("https://i.imgur.com/SYGokPF.png","https://i.imgur.com/Kd54e7i.png"),
    ## Expert Answer
    ("https://i.imgur.com/I2XIxyR.gif","https://i.imgur.com/RYrP58D.gif"),
    

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
     
    



    ########### FAQs #####################
    
    ## Log in
    ("https://i.imgur.com/UX8V7XZ.png","https://i.imgur.com/kgHm6uz.png"),
    ## Machine Selection
    ("https://i.imgur.com/yKOvFFR.png","https://i.imgur.com/1EBP4vW.png"),
    ## Upload Documents
    ("https://i.imgur.com/UEWdM88.png","https://i.imgur.com/SQl80JG.png"),
    ## Search
    ("https://i.imgur.com/sSzwMzB.png","https://i.imgur.com/lNhW1ZX.png"),
    ## Language 1
    ("https://i.imgur.com/5VxkZGp.png"," https://i.imgur.com/Og51HWt.png "),
    ## Language 2
    ("https://i.imgur.com/NYOlzKn.png"," https://i.imgur.com/HIC2qkY.png"),
    ## Reset password
    ("https://i.imgur.com/puiD8Wa.png","https://i.imgur.com/10hlFfM.png"),
    ## Search uploaded docs
    ("https://i.imgur.com/fF703fJ.png","https://i.imgur.com/T242eAD.png"),
    ## Search page
    ("https://i.imgur.com/7CEiZF8.png","https://i.imgur.com/DK6n4aa.png"),
    


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
