import os

class DEMReader:
   def __init__(self) -> None:
      pass

   def read_file(self, path):
      f = open(path, 'r')
      for line in f:
         print(line)
      f.close()   
      pass 

   def read_folder(self, path):
      folders = os.listdir(path)
      for file in folders:
         f = open(path, 'r')
         for line in file:
            continue
         f.close()   
      pass  