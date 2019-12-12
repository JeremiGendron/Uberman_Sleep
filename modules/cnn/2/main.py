import time
from datetime import datetime
import numpy as np
import tensorflow as tf
from tensorflow import keras

data = np.memmap('./data/data_concat.npy', shape=(400000, 2000, 2), dtype=float, mode='r')
labels = np.load('./data/labels_shifted.npy', allow_pickle=True)

print(labels.shape, data.shape)

model = keras.Sequential([
  keras.layers.Conv1D(2000, 2, strides=1, activation='relu', input_shape=(2000,2), batch_size=100),
  keras.layers.BatchNormalization(),
  keras.layers.MaxPooling1D(2, 2),
#  keras.layers.Conv1D(32, 10, strides=1, activation='relu'),
#  keras.layers.BatchNormalization(),
#  keras.layers.MaxPooling1D(2, 2),
#  keras.layers.UpSampling1D(2),
#  keras.layers.Conv1D(32, 2, strides=1, activation='relu'),
#  keras.layers.BatchNormalization(),
  keras.layers.Flatten(),
  keras.layers.Dense(56, activation='relu'),
  keras.layers.Dense(56, activation='relu'),
  keras.layers.Dense(1, activation='sigmoid')
])

callbacks = [
  keras.callbacks.ModelCheckpoint('models/', monitor='val_acc', verbose=0, save_best_only=True, mode='auto', period=3),
  keras.callbacks.EarlyStopping(monitor='val_acc', min_delta=0.001, patience=0, verbose=0, mode='auto', restore_best_weights=False)
]

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(data[:40000], labels[:40000], validation_split=0.1)
