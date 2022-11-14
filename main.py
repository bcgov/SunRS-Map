import os   #  Usages: get_folders()
import sys  #  Usages: main()
from Region import Region
from DEMReader import DEMReader as dem_reader


# How do we want to render this? As a point on a map?
def render():
   pass


def print_values(values):
   print(values)


def main():
   print_values("Starting the thing")
   data_path = sys.path[0] + '/data'
   demr = dem_reader(data_path)
   demr.read_folder(data_path)
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
