import os   #  Usages: get_folders()   
import sys  #  Usages: main()
from DEMReader import DEMReader

def print_values(values):
   print (values)

# Given a folder path, return list of folders in specified folder.
# TODO: Add check if path valid
def get_folders(path):
   temp_folders = []                   # type list(string)
   current_folder = os.listdir(path)   # type list(string)
   for folder in current_folder:
      if(os.path.isdir(os.path.join(path, folder))):
         temp_folders.append(folder)
   return temp_folders

def main():
   print_values("Starting the thing")
   workingDir = sys.path[0]         # type string
   dataPath = workingDir + '/data'  # type string
   folderList = get_folders(dataPath)  # type list(string)
   dem = DEMReader()

   regions = []   # type list(regions)
   
   for folder in folderList:
      tempPath = dataPath + "/" +folder
      files = os.listdir(tempPath)
      for file in files:
         tempPath = tempPath + "/" + file
         dem.read_file(tempPath)
   print_values("Done the thing")

   pass

main()