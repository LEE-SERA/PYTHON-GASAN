# -*- coding: utf-8 -*-
"""ANN_MNIST_Classification_이세라.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/108_ZyPBvJeb8vAl1apNj05EHHl1ZbPGG
"""

import numpy as np
from keras import layers,models,datasets
from keras.utils import np_utils
import matplotlib.pyplot as plt

def ANN_Model(nIn,nHidden,nOut):
  x = layers.Input(shape=(nIn,))
  h = layers.Activation('relu')(layers.Dense(nHidden)(x))
  y = layers.Activation('softmax')(layers.Dense(nOut)(h))

  model = models.Model(x,y)
  model.compile(loss = 'categorical_crossentropy',
                optimizer ='adam', metrics =['accuracy'])
  return model

def Data_func():
  (x_train,y_train),(x_test,y_test) = datasets.mnist.load_data()
  y_train = np_utils.to_categorical(y_train)
  y_test = np_utils.to_categorical(y_test)

  L,W,H = x_train.shape
  x_train = x_train.reshape(-1,W*H)
  x_test = x_test.reshape(-1,W*H)      #행렬모양을 1차원으로 만듬 

  x_train = x_train /225.0
  x_test = x_test /255.0

  return (x_train,y_train),(x_test,y_test)

def plot_loss(history):
  plt.plot(history.history['loss'])
  plt.plot(history.history['val_loss'])
  plt.title('Model loss')
  plt.ylabel('loss')
  plt.xlabel('Epochs')
  plt.legend(['Train', 'Test'],loc =100)

def plot_acc(history):
  plt.plot(history.history['acc'])
  plt.plot(history.history['val_acc'])
  plt.title('Model accuracy')
  plt.ylabel('Accutacy')
  plt.xlabel('Epochs')
  plt.legend(['Train', 'Test'],loc =0)

nIn = 784
nHidden = 200
nHidden2 = 100
nClass =10
nOut = nClass

model= ANN_Model(nIn,nHidden,nOut)
(x_train,y_train),(x_test,y_test) = Data_func()

#print(x_train[0])
plt.imshow(x_train[4])
#print(x_train.shape) #(60000,28,28),



history = model.fit(x_train,y_train, epochs = 15,
                    batch_size =100,validation_split =0.2)

performance_test = model.evaluate(x_test,y_test,batch_size =100)
print('Test Loss and Accuracy->', performance_test)

plot_loss(history)
plt.show()
plot_acc(history)
plt.show()
#layer 추가
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
def ANN_Model_Sequential(nIn,nHidden,nOut):
  model =Sequential()
  model.add(Dense(nHidden,input_shape=(nIn,),activation='relu'))
  model.add(DENSE(nHidden2, input_shape=(nIn),activation ='relu'))
  model.add(Dense(nOut,activation ='softmax'))

  opt =Adam(learning_rate=0.001)
  model.compile(opt,loss ='categorical_crossentrophy',metrics=['accuracy'])
  return

