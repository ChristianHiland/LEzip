from zipfile import ZipFile
import json
import glob
import os

class LeZip:
    def __init__(self, File, DirName):
        pass
    def Make(self, File, DirName):
        with ZipFile(File, 'a') as Zipfile:
            with Zipfile.open(File, 'w') as zip:
                # Iterate over all the files in directory
                for folderName, subfolders, filenames in os.walk(DirName):
                    for filename in filenames:
                        #create complete filepath of file in directory
                        filePath = os.path.join(folderName, filename)
                        # Add file to zip
                        zip.write(filePath, basename(filePath))
    def Read(self):
        print("Read")
    def Extract(self):
        print("Extract")