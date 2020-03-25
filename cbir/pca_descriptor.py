from sklearn.decomposition import PCA
import pickle

class PCADescriptor:
  def __init__(self, imgs):
    self.imgs = imgs

  def describe(self):
    pca = PCA(n_components=100).fit(self.imgs)
    
    return pca
  


