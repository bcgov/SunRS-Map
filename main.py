from Sample import Sample

def compare_scores():
   pass

def render():
   pass

def print_values(values):
   print (values)

def get_folders():
   # Go through the data folder and get all values of items that are of type .dir
   # Return list
   #TODO: Sam do this
   pass

def main():
   print_values("Starting the thing")
   folders = get_folders()

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

