import os 
import shutil

path = '/Users/chaitalishah/Desktop/Krsna_WHJ/Classes/Class-102'
source = '/Users/chaitalishah/Desktop/Krsna_WHJ/Classes/Class-102/assets'
destination = '/Users/chaitalishah/Desktop/Krsna_WHJ/Classes/Class-102/move_here'

list = os.listdir(source)

for count in list:
    name, extension = os.path.splitext(count)

    if extension == "":
        continue
    
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1 = source + "/" + count
        path2 = destination + "/" + "Image Files"
        path3 = destination + "/" + "Image Files" + count

        if os.path.exists(path2):
            print("Moving file to",destination,".....")
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("Moving file to",destination,".....")
            shutil.move(path1,path2)