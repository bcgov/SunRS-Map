import os
class Point:
   # Will a point be an area or a single lat lon value?
   def __init__(self, lat, lon) -> None:
      self.score            = 0 # To be set in District.py
      self.lat              = 0 
      self.lon              = 0
      self.elevation        = 0
    
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

   def set_elevaton(self, elevation):
      self.elevation = elevation
