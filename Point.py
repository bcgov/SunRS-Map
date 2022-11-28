import os


class Point:
   # Will a point be an area or a single lat lon value?
   def __init__(self, lat, lon, elevation) -> None:
      self.lat              = lat
      self.lon              = lon
      self.elevation        = elevation
      self.set_score(elevation)
      self.score            = self.get_score()
    
   def get_score(self):
      return self.score

   def set_score(self, score):
      self.score = score

   def get_lat(self):
      return self.lat

   def set_lat(self, lat):
      self.lat = lat

   def get_lon(self):
      return self.lon

   def set_lon(self,lon):
      self.lon = lon

   def get_elevation(self):
      return self.elevation

   def set_elevation(self, elevation):
      self.elevation = elevation

   def calculate_score(self):
      self.set_score(self.get_elevation())
