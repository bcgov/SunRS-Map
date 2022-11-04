import os
class District:
   def __init__(self, fileName) -> None:
      self.fileName  = fileName
      self.point_scores      = []                        # Scores of all locations in Sample folder (Ordered from highest to lowest? If we sort while we insert, the search for highest score will be quicker)
      self.district_score         = 0
      self.read_file_in_folder(self.folderName)