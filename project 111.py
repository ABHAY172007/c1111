import os
import shutil
#print(dir(os))
os.getcwd()
#os.mkdir("abhay")
path=os.listdir("C:/Users/abhay/OneDrive/Desktop")
print(path)
path1=os.path.exists("C:/Users/abhay/OneDrive/Desktop/avg")
print(path1)
imgpath="C:/Users/abhay/OneDrive/Desktop/bg1.JPG"
root,extension=os.path.splitext(imgpath)
print("the root of the image is",root)
print("the extension of the image is",extension)
source="C:/Users/abhay/OneDrive/Desktop/source"
destination="C:/Users/abhay/OneDrive/Desktop/destination"
move=shutil.move(source,destination)
print("it is done")
