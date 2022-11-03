import os   #  Usages: get_folders()   
import sys  #  Usages: main()
from Sample import Sample

def compare_scores():
   pass

def render():
   pass

def print_values(values):
   print (values)

# Given a folder path, return list of folders in specified folder.
def get_folders(path):
   temp_folders = []
   curFolders = os.listdir(path)
   for folder in curFolders:
      if(os.path.isdir(os.path.join(path, folder))):
         temp_folders.append(folder)
   return temp_folders

   # Go through the data folder and get all values of items that are of type .dir
   # Return list
   #TODO: Sam do this
   pass

def main():
   print_values("Starting the thing")
   workingDir = sys.path[0]
   folders = get_folders(workingDir + '/data')

   samples = []
   # TODO: Sam do this part too
   for file in folders:
      temp = Sample(file)
      samples.append(temp)

   print_values("Done the thing")

   pass

main()


# Where is the greatest _____ in this sample area
# Score directly impacts what the greatest ___ means

# Extracts our data from our source files
# give a score to the sources files
# act based on that score


# set_score_highest()
# set_score_lowest()
# assign_score really complicated 

