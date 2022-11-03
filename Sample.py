import os
class Sample:
   def __init__(self, folderName) -> None:
      self.folderName  = folderName
      self.scores      = []
      self.read_file_in_folder(self.folderName)

   def read_file_in_folder(self, folderName):

      folder = os.listdir(folderName)
      for file in folder:
         print (file)
         f = open(file, "r")
         for line in file:
            self.scores.append(self.find_highest_point(line))
         f.close()
      pass
   
   def find_highest_point(self, value):
      temp = 0
      if (value > temp):
         temp = value
      return value

   def compute_score(self):
      # find biggest number
      highest_point = 0


      self.set_score(highest_point)
      pass

   def set_score(self, value):
      self.score = value

   