from Point import Point


class Zone:
   def __init__(self, name) -> None:
      self.name            = name
      self.sub_zones       = []
      self.best_sub_zone   = Zone or Point
      self.score           = 0

   def get_name(self):
      return self.name

   def set_name(self, name):
      self.name = name

   def get_sub_zones(self):
      return self.sub_zones

   def set_sub_zones(self, sub_zones_list):
      self.sub_zones = sub_zones_list

   def add_to_sub_zones(self, sub_zone):
      self.sub_zones.append(sub_zone)

   def get_best_sub_zone(self):
      return self.best_sub_zone

   def set_best_sub_zone(self, sub_zone):
      self.best_sub_zone = sub_zone

   def get_score(self):
      return self.score

   def set_score(self, score):
      self.score = score

   def calculate_score(self):
      if self.sub_zones:
         for sub_zone in self.sub_zones:
            sub_zone.calculate_score()
         self.sort_sub_zones()
         self.set_best_sub_zone(self.sub_zones[0])
         self.set_score(self.get_best_sub_zone().get_score())
      else:
         print("Sub_zone list is empty")

   def sort_sub_zones(self):
      self.sub_zones.sort(key=lambda subzone: subzone.get_score(), reverse=True)

   def is_zone(self):
      return True

   def get_coords(self):
      if self.get_best_sub_zone().is_zone():
         return self.get_best_sub_zone().get_coords()
      else:
         return self.get_best_sub_zone()
