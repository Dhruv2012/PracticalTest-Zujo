#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 10:09:47 2019

@author: dhruv
"""

from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

DATASET_PATH = '/home/dhruv/PracTest_Zujo/Problem2/Final_Dataframe.csv'
# Path to the dataset specified
nRowsRead = 1000 # specify 'None' if want to read whole file
df1 = pd.read_csv(DATASET_PATH, delimiter=',', nrows = nRowsRead)
df1.dataframeName = 'Final_Dataframe.csv'
nRow, nCol = df1.shape
print(" ")
print(f'There are {nRow} rows and {nCol} columns')
df_array = df1.iloc[:,:].values
print(" ")
print("data array is:")
print(df_array)
print(" ")
print(" ")

# PRE-PROCESSING THE CATEGORICAL DATA AND CONVERTING IT TO NUMERICAL DATA FOR APPLYING CLUSTERING TECHNIQUE.
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder = LabelEncoder()
df_array[:,0] = labelencoder.fit_transform(df_array[:,0])
df_array[:,1] = df_array[:,1].astype(str)
df_array[:,1] =  labelencoder.fit_transform(df_array[:,1])
df_array[:,3] =  labelencoder.fit_transform(df_array[:,3])
df_array[:,4] =  labelencoder.fit_transform(df_array[:,4])
df_array[:,5] =  labelencoder.fit_transform(df_array[:,5])
df_array = np.array(df_array)
temp = df_array[:,8]
temp = temp.reshape(-1,1)
for i in range(0,205):
    x = temp[i,0]
    index = 0
    y = ''
    while(x[-1] !='/'):
        x = x[:-1]
    x = x[:-1]
    temp[i,0] = x
df_array[:,8] = df_array[:,8].astype(float)

onehotencoder = OneHotEncoder(categorical_features=[0,1,3,4,5])
df_array= onehotencoder.fit_transform(df_array).toarray()
print(" ")
print("After performing OneHOt Encoding data array is:")
print(df_array)

# K-MEANS CLUSTERING
from sklearn.cluster import KMeans
wcss = []
# CHOOSING THE OPTIMIZED NO. OF CLUSTERS FROM THE GRAPH
for i in range(1,12):
    kmeans = KMeans(n_clusters=i,init='k-means++', max_iter=300,n_init=10)
    kmeans.fit(df_array)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,12),wcss)
plt.title('THe Elbow Method')
plt.xlabel('no. of clusters')
plt.ylabel('WCSS')
plt.show()

# NO. OF CLUSTERS = 5 FROM THE GRAPH
kmeans = KMeans(n_clusters=5,init='k-means++',max_iter=300,n_init=10)
y_means= kmeans.fit_predict(df_array)
df1['label'] = y_means
#  Visualizing the CLuster ACROSS 2 dimensions among 256 dimensions
plt.scatter(df_array[y_means==0,253], df_array[y_means==0,255], s=100, c='red', label='Cluster1')
plt.scatter(df_array[y_means==1,253], df_array[y_means==1,255], s=100, c='blue', label='Cluster2')
plt.scatter(df_array[y_means==2,253], df_array[y_means==2,255], s=100, c='green', label='Cluster3')
plt.scatter(df_array[y_means==3,253], df_array[y_means==3,255], s=100, c='cyan', label='Cluster4')
plt.scatter(df_array[y_means==4,253], df_array[y_means==4,255], s=100, c='magenta', label='Cluster5')
plt.title('CLUSTER')
plt.xlabel('discount price')
plt.ylabel('rating ')
plt.legend()
plt.show()

cluster1 = df1[df1.label==0]
cluster2 = df1[df1.label==1]
cluster3 = df1[df1.label==2]
cluster4 = df1[df1.label==3]
cluster5 = df1[df1.label==4]


# 5 different clusters here represent 5 different types of recommendations for laptops


# RECOMMENDATION PART
# CHOOSING A LAPTOP FROM THE df_array[i] and printing its recommended laptops from the clusters
i = 4 
test_laptop = df_array[i]
print(" ")
print(" ")
print("The laptop information used for testing is:")
print(df1[df1.index == i])
label = y_means[i]
print(" ")
print(" ")
print("The recommended laptops are:")
print(df1[df1.label==label])





