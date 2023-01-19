import tensorflow as tf
from tensorflow import keras

def model(data_shape, neurons):

    mdl = tf.keras.Sequential()    
    mdl.add(tf.keras.layers.LSTM(
        neurons,
        input_shape=(data_shape,1)
        ))
    mdl.add(tf.keras.layers.Dropout(0.1))
    mdl.add(tf.keras.layers.BatchNormalization())
    mdl.add(tf.keras.layers.Dense(32))
    mdl.add(tf.keras.layers.Dense(32))
    mdl.add(tf.keras.layers.Dense(1))

    optimizer = keras.optimizers.Adam(learning_rate=1e-3, weight_decay=1e-4)
    mdl.compile(loss='mae', optimizer=optimizer)
    
    return mdl
