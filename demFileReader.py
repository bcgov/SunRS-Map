import numpy as np
import rasterio as rio
from rasterio.plot import show
import matplotlib.pyplot as plt

path = "data/95a/095a01_e.dem"

dem = rio.open(path)
dem_array = dem.read(1).astype('float64')


fig, ax = plt.subplots(1, figsize=(12, 12))

show(dem_array, cmap='Greys_r', ax=ax)

plt.axis("off")
plt.show()


with rio.open(path) as f:
    arr = f.read(1)
    mask = (arr != f.nodata)
    elev = arr[mask]
    col, row = np.where(mask)
    x, y = f.xy(col, row)
    uid = np.arange(f.height * f.width).reshape((f.height, f.width))[mask]

result = np.rec.fromarrays([uid, x, y, elev],
                           names=['id', 'x', 'y', 'elev'])

print(result.dtype)
print(result[:10])
