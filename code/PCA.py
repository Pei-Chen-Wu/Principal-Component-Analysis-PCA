# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:47:32 2020

@author: Nclab
"""

import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
# make_nlobs方法常被用來生成聚類算法的測試數據 
# make_blobs會根據用戶指定的特徵數量，中心點數量，範圍等來生成幾類數據 
from sklearn.datasets.samples_generator import make_blobs 
# X為樣本特徵，Y為樣本簇類型 共10000個樣本，每個樣本3個特徵，共4個簇 
# n_samples表示產生多少個數據 n_features表示數據是幾維， 
# centers表示中心點 cluster_std表示分布的標準差 
X, y = make_blobs(n_samples=10000, n_features=3, centers=[[3, 3, 3], [0, 0, 0], [1, 1, 1], [2, 2, 2]], cluster_std=[0.2, 0.1, 0.2, 0.2], random_state=9) 
fig = plt.figure() 
ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=30, azim=20) 
plt.scatter(X[:, 0], X[:, 1], X[:, 2], marker='o') 
plt.show()


from sklearn.decomposition import PCA
pca = PCA(n_components=3) 
pca.fit(X) 
print('三個特徵維度的方差比例:',pca.explained_variance_ratio_)
print('三個特徵維度的方差:',pca.explained_variance_)

#降維
pca = PCA(n_components=2) 
pca.fit(X) 
print('兩個特徵維度的方差比例:',pca.explained_variance_ratio_) 
print('兩個特徵維度的方差:',pca.explained_variance_)

X_new = pca.transform(X) 
plt.scatter(X_new[:, 0], X_new[:, 1],marker='o') 
plt.show()
