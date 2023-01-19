import tensorflow as tf
import pandas as pd
import numpy as np
import model as md
import datasets as ds
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '3'

num_epochs = 10
num_neurons = 100
train_csv = 'AAPL.csv'
test_csv = 'LMT.csv'


def save_model(model):
    model.save('tfmodel')


def main():
    train_x,train_y,test_x,test_y = ds.load_data(train_csv, test_csv)
    data_shape = train_x.shape[1]
    model = md.model(data_shape, num_neurons)


    model.fit(train_x, train_y, epochs=num_epochs, validation_data=(test_x,test_y))
    test_predictions = model.predict(test_x)
    

    mae = np.mean(np.abs(test_predictions - test_y.values[0]))
    try:
        print(test_predictions[-10:])
        #print(test_predictions)
    except:
        print('You fucked up')
    print("Mean Absolute Error: {:.2f}".format(mae))

    # Uncomment to save the model once a functioning one has been found
    #save_model(model)


if tf.config.list_physical_devices('GPU'):
    print("Using GPU for training")
    with tf.device('GPU:0'):
        main()

else:
    print("No GPU available, using CPU for training")
    main()