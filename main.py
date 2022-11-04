import os   #  Usages: get_folders()   
import sys  #  Usages: main()
from Sample import Sample

# Given 2 scores (or samples) compare and return > 0 if the first is higher, 0 if equal, < 0 if less (Could do 1, 0, -1 but I wanted to try this.)
def compare_scores(score1, score2):
   return score1 - score2
   pass

# How do we want to render this? As a point on a map?
def render():
   pass

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

   # Go through the data folder and get all values of items that are of type .dir
   # Return list
   #TODO: Sam do this

# Returns the sample with the highest score
def get_highscore(sample_List):
   max_val = 0    # type int
   max_sample = 0 # type Sample
   for sample in sample_List:
      if(sample.get_score() > max_val):
         max_val = sample.get_score()
         max_sample = sample
   return max_sample

def main():
   print_values("Starting the thing")
   workingDir = sys.path[0]         # type string
   dataPath = workingDir + '/data'  # type string
   folderList = get_folders(dataPath)  # type list(string)

   samples = []   # type list(Samples)
   
   for folder in folderList:
      temp = Sample(dataPath +"/" + folder)  # type Sample
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

