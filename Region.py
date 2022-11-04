import os
class Region:
   def __init__(self, folderName) -> None:
      self.folderName  = folderName
      self.district_scores      = []                        # Scores of all locations in Sample folder (Ordered from highest to lowest? If we sort while we insert, the search for highest score will be quicker)
      self.region_score         = 0
      self.read_file_in_folder(self.folderName)

   def read_file_in_folder(self, folderName):

      folders = os.listdir(folderName)
      for file in folders:
         f = open(folderName+"/"+file, "r")
         for line in file:
            self.district_scores.append(self.find_highest_point(line))
         f.close()
      pass
   
   def find_highest_point(self, value):
      temp = 0
      intValue = int(value)
      if (intValue > temp):
         temp = intValue
      return intValue

   # Computes the score of a district
   def compute_score(self):
      # find biggest number

      highest_point = 0


      self.set_region_score(highest_point)
      pass      

   def get_region_score(self):
      pass

   def set_region_score(self, value):
      self.region_score = value

   def get_score(self, value):
      return self.region_score

   def print_region(self):
      print(self.folderName)
      print(self.get_score())


# (Lat. 48°17′52.9″ N) to Lat. 60°
# Latitude     E-W Spacing    N-S Spacing
#    45           65.5m          92.6m
#    50           119.1m         92.7m
#    55           106.3m         92.7m
#    60           92.6m          92.8m
      
 