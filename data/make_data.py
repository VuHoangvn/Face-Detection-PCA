import os
import shutil

dir_src = ["raw/s" + str(i) for i in range(1,51)]

dir_dst = "imgs"
i = 1
for fold in dir_src:
  for filename in os.listdir(fold):
    if filename.endswith('.pgm'):
      shutil.copy(fold + '/' +filename, dir_dst)
      os.rename(dir_dst+'/' + filename, dir_dst + '/' + str(i) + '.pgm')
      i += 1
    
