import argparse
from cbir import PCADescriptor
import os
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required=True,
	help = "Path to where the features index will be stored")
args = vars(ap.parse_args())

output = args["index"]
imagePaths = os.listdir(args["dataset"])
imgs = []
filenames = []
for imagePath in imagePaths:
  image = cv2.imread(args["dataset"] + "/" + imagePath, cv2.IMREAD_GRAYSCALE)

  imgs.append(image)
  filenames.append(imagePath)

# print(filenames)
imgs = np.asarray(imgs)
print(imgs.shape)

pca = PCADescriptor(imgs)
features = pca.describe()

with open(output, "w") as f:
  for filename, feature in zip(filenames, features):
    f.write("{},{}\n".format(filename, ",".join(feature)))

