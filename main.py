import os   #  Usages: get_folders()   
import sys  #  Usages: main()
from Sample import Sample

# Given 2 scores (or samples) compare and return > 0 if the first is higher, 0 if equal, < 0 if less (Could do 1, 0, -1 but I wanted to try this.)
def compare_scores(score1, score2):
   return score1 - score2
   pass

def render():
   pass

def print_values(values):
   print (values)

# Given a folder path, return list of folders in specified folder.
# TODO: Add check if path valid
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


def main():
   print_values("Starting the thing")
   workingDir = sys.path[0]
   dataPath = workingDir + '/data'
   folderList = get_folders(dataPath)

   samples = []
   # TODO: Sam do this part too
   
   for folder in folderList:
      temp = Sample(dataPath +"/" + folder)
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

