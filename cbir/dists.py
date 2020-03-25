import numpy as np 

def chi2_distance(pca1, pca2, eps=1e-10):
  # compute the chi-squared distance
  d = 0.5 * np.sum((pca1-pca2) ** 2 / (pca1+pca2+eps))

  return d