import os, shutil
casFilePath = "ClientAppSettings.json"

robloxDirectory = f"{os.getenv('LOCALAPPDATA')}/Roblox/Versions/"
robloxDirContents = os.listdir(robloxDirectory)

# create folder in roblox version called "ClientSettings", then put json inside folder

for fileName in robloxDirContents:
    path = robloxDirectory + fileName
    if os.path.isdir(path):
        print(fileName + " is a version folder")
        print(os.listdir(path))
        if not os.path.exists(path + "/ClientSettings"):
          os.mkdir(path + "/ClientSettings")
          shutil.copyfile(casFilePath, path + "/ClientSettings/ClientAppSettings.json")
        else:
           print("ClientSettings already exists")
          
        
