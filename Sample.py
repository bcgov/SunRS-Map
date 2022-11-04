import os
class Sample:
   def __init__(self, folderName) -> None:
      self.folderName  = folderName
      self.scores      = []                        # Scores of all locations in Sample folder (Ordered from highest to lowest? If we sort while we insert, the search for highest score will be quicker)
      self.read_file_in_folder(self.folderName)

   def read_file_in_folder(self, folderName):

      folders = os.listdir(folderName)
      for file in folders:
         f = open(folderName+"/"+file, "r")
         for line in file:
            self.scores.append(self.find_highest_point(line))
         f.close()
      pass
   
   def find_highest_point(self, value):
      temp = 0
      intValue = int(value)
      if (intValue > temp):
         temp = intValue
      return intValue

   def compute_score(self):
      # find biggest number

      highest_point = 0


      self.set_score(highest_point)
      pass

   def set_score(self, value):
      self.score = value

   def get_score(self, value):
      return self.score

   def print_sample(self):
      print(self.folderName)
      print(self.get_score())
      
 