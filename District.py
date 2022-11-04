import os
class District:
   def __init__(self, filename) -> None:
      self.filename           = filename
      self.point_scores       = []                        # Scores of all locations in Sample folder (Ordered from highest to lowest? If we sort while we insert, the search for highest score will be quicker)
      self.best_point         = 0
      self.district_score     = 0
      self.read_point_in_file(self.fileName)

   def get_filename(self):
      pass

   def get_point_scores(self):
      pass

   def get_best_point(self):
      pass

   def read_point_in_file(self):
      pass

   