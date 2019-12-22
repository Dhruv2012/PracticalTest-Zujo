#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 13:49:52 2019

@author: dhruv
"""

from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import matplotlib.image as mpimg
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os # accessing directory structure

DATASET_PATH = '/home/dhruv/PracTest_Zujo/Problem3/fashion-product-images-small/myntradataset/'
print(os.listdir(DATASET_PATH))

df = pd.read_csv(DATASET_PATH + "styles.csv", nrows=6000)
df['image'] = df.apply(lambda x: str(x['id']) + ".jpg",axis = 1)
df = df.reset_index(drop=True)
df.head(10)

import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.layers import GlobalMaxPooling2D
import keras
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

df.articleType.value_counts().sort_values().plot(kind='barh')
print(df['image'][0])

def plot_figures(figures, nrows = 1, ncols=1,figsize=(8, 8)):
    fig, axeslist = plt.subplots(ncols=ncols, nrows=nrows,figsize=figsize)
    for ind,title in enumerate(figures):
        axeslist.ravel()[ind].imshow(figures[title])
        axeslist.ravel()[ind].set_title(title)
        axeslist.ravel()[ind].set_axis_off()
    plt.tight_layout() # optional

figures = {'im'+str(i): load_img(DATASET_PATH + "images/" + str(row.image)) for i, row in df.sample(6).iterrows()}
plot_figures(figures, 2, 3)

temp = Image.open(DATASET_PATH + "images/" + str(df.iloc[0].image))
(w,h,) = temp.size

base_model = ResNet50(weights='imagenet', 
                      include_top=False, 
                      input_shape = (w, h, 3))
base_model.trainable = False
base_model.summary()
model = tf.keras.Sequential([
    base_model,
    GlobalMaxPooling2D()
])
model.summary()

import swifter
def img_path(img):
    return DATASET_PATH+"images/"+img

def get_embedding(model, img_name):
    img = load_img(img_path(img_name), target_size=(w, h))
    x   = img_to_array(img)
    x   = np.expand_dims(x, axis=0)
    x   = preprocess_input(x)
    return model.predict(x).reshape(-1)

# 
df['embedding'] = df['image'].swifter.apply(lambda img: get_embedding(model, img))
df_embs = df['embedding'].apply(pd.Series)

