import os
import numpy as np
import seaborn as sns
import rasterio as rio
from rasterio.plot import show
from rasterio.merge import merge
import matplotlib.pyplot as plt
import glob
import earthpy as et
import earthpy.plot as ep
from District import District
from Zone import Zone


class DEMReader:
   def __init__(self) -> None:
      pass

   def read_file(self, path):
      dem = rio.open(path)
      zone = Zone(path)
      zone.set_sub_zones(dem.read(1, masked=True))
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
            print(fpath + " Is not a folder or a file")
      return zone

   def show_map(self, display_type):
      self.map_setup()
      ep.plot_bands(self.dem_data,
                    title="Lidar Digital Elevation Model (DEM)",
                    cmap="Greys")
      plt.show(cmap=display_type)

   def map_setup(self):
      sns.set(font_scale=1.5, style="white")

   # Values at -32767 mean there was no data
