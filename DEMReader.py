import os
import numpy as np
import rasterio as rio
from rasterio.plot import show
from rasterio.merge import merge
import matplotlib.pyplot as plt
import glob


class DEMReader:
   def __init__(self, data_path) -> None:
      self.data_path = data_path
      self.read_folder(data_path)
      pass

   def read_file(self, path):
      dem = rio.open(path)
      dem_array = dem.read(1).astype('float64')
      fig, ax = plt.subplots(1, figsize=(12, 12))
      show(dem_array, cmap="Greys_r", ax=ax)
      plt.axis("off")
      plt.show()
      return 1

   def read_folder(self, path):
      folders = os.listdir(path)
      for f in folders:
         fpath = os.path.join(path, f)
         if os.path.isdir(fpath):
            self.read_folder(fpath)
         elif os.path.isfile(fpath):
            self.read_file(fpath)
         else:
            print(fpath + " Is not a folder or a file")
      return 1
