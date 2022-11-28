import os
import numpy as np
import rasterio as rio
from rasterio.plot import show
from rasterio.merge import merge
import matplotlib.pyplot as plt
from Zone import Zone
from Point import Point


class DEMReader:
   def __init__(self) -> None:
      pass

   def read_file(self, path):
      zone = Zone(path)

      result = self.eval_dem_file(path)
      result.sort(order='elev')
      descending_result = result[::-1]

      for point in descending_result[:10]:                  # Will only store the top 10 values in the file. Will need to expand this in the future
         new_point = Point(point[1], point[2], point[3])    # X,Y,elevation
         zone.add_to_sub_zones(new_point)
      zone.calculate_score()
      print(zone.get_score())

      return zone

   def read_folder(self, path):
      folders = os.listdir(path)
      zone = Zone(path)
      for f in folders:
         fpath = os.path.join(path, f)
         if os.path.isdir(fpath):
            zone.add_to_sub_zones(self.read_folder(fpath))
         elif os.path.isfile(fpath):
            zone.add_to_sub_zones(self.read_file(fpath))
         else:
            print(fpath + " Is not a folder or a file?")
      return zone

   def eval_dem_file(self, path):
      with rio.open(path) as f:
         arr = f.read(1)
         mask = (arr != f.nodata)
         elev = arr[mask]
         col, row = np.where(mask)
         x, y = f.xy(col, row)
         uid = np.arange(f.height * f.width).reshape((f.height, f.width))[mask]
         return np.rec.fromarrays([uid, x, y, elev], names=['id', 'x', 'y', 'elev'])

   # Values at -32767 mean there was no data

