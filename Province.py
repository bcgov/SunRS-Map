import os
from Region import Region


class Province:
   def __init__(self, province) -> None:
      self.province = province
      self.regions = []  # Scores of all locations in Sample folder (Ordered from highest to lowest? If we sort while we insert, the search for highest score will be quicker)
      self.best_region = 0

   def get_province(self):
      return self.province

   def get_regions(self):
      return self.regions

   def add_region(self, region):
      self.regions.append(region)

   def get_best_regions(self):
      return self.best_region

   def set_best_regions(self, region):
      self.best_region = region
