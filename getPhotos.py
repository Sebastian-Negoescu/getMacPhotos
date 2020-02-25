import os
import fnmatch
from os import path
from datetime import date, time, datetime

myUser = path.dirname(os.getcwd())
today = datetime.date(datetime.today())
photoCollection = []
print(f"Today is: {today}")
print(f"My user path is: {myUser}")
photosDir = path.join(f"{myUser}/Pictures/Photos Library.photoslibrary/originals/")
print(f"My photos directory is located at: {photosDir}")
for root, dir, files in os.walk(photosDir):
    for i, fileName in enumerate(files):
        absFilePath = os.path.join(photosDir, root, fileName)
        fileMtime = os.stat(absFilePath).st_mtime
        fileDateTime = datetime.fromtimestamp(fileMtime).date()
        print(f"{absFilePath} modified at: {fileDateTime}")
        print(f"Today is type: {type(today)}")
        print(f"FileDateTime is type: {type(fileDateTime)}")
        if (fileDateTime >= today):
            print(f"FOUND FILE:{absFilePath}")
            photoCollection.append(absFilePath)
print("Finished searching - all the files found are printed below:")
for photoFile in photoCollection:
    print(photoFile)
