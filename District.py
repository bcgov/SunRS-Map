import os
from Point import Point

class District:
   def __init__(self, filename) -> None:
      self.filename           = filename
      self.points       = []                        # Scores of all locations in Sample folder (Ordered from highest to lowest? If we sort while we insert, the search for highest score will be quicker)
      self.best_point         = 0
      self.district_score     = 0                   # Assigned by Region.py
      self.read_point_in_file(self.fileName)

   def get_filename(self):
      pass

   def get_points(self):
      pass

   def get_best_point(self):
      pass

   def get_district_score(self):
      pass

   def set_best_point(self, point):
      pass

   def read_point_in_file(self):
      pass

   def find_best_point(self):
      pass

   def add_point(self, point):
      pass

   