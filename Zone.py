class Zone:
   def __init__(self, name) -> None:
      self.name            = name
      self.sub_zones       = []
      self.best_sub_zone   = 0
      self.zone_score      = 0

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

   def get_zone_score(self):
      return self.zone_score

   def set_zone_score(self, zone_score):
      self.zone_score = zone_score
