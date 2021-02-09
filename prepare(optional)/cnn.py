import json
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras
from keras.models import load_model

data_path = 'newDataSet.json' #name of your data set

def load_data(data_path):
    with open(data_path,'r') as fp:
        data = json.load(fp)

    x = np.array(data['mfcc'])
    y = np.array(data['labels'])
    y = correct_y(y)
    return x,y

def correct_y(Y):
    new_y = np.zeros((Y.shape[0],10))
    for i in range(Y.shape[0]):
        new_y[i][Y[i]] = 1
    return new_y

def prepare_datasets(test_size,validation_size):
    #load data from path
    X,Y = load_data(data_path)
    #split to train and test
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size= test_size)
    #split to train and validation
    X_train,X_validation,Y_train,Y_validation = train_test_split(X_train,Y_train,test_size= validation_size)
    #change axis from 3 to 4
    X_train = X_train[...,np.newaxis]
    X_validation = X_validation[...,np.newaxis]
    X_test = X_test[...,np.newaxis]

    return X_train,X_validation,X_test,Y_train,Y_validation,Y_test

def build_network(input_shape):
    #creat model
    model = keras.Sequential()
    # conv layer
    model.add(keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=input_shape))
    # conv layer
    model.add(keras.layers.Conv2D(32,(3,3),activation='relu'))
    # maxpooling layer
    model.add(keras.layers.MaxPooling2D((3,3),strides=(2,2),padding='same'))
    # dropout
    model.add(keras.layers.Dropout(0.25))
    #conv layer
    model.add(keras.layers.Conv2D(32,(3,3),activation='relu'))
    # maxpooling layer
    model.add(keras.layers.MaxPooling2D((3,3),strides=(2,2),padding='same'))
    #dropout conv layer
    model.add(keras.layers.Dropout(0.25))
    #Flatten layer too feed it into dence layer
    model.add(keras.layers.Flatten())
    #dense layer
    model.add(keras.layers.Dense(64,activation='relu'))
    # dropout
    model.add(keras.layers.Dropout(0.5))
    #dense layer
    model.add(keras.layers.Dense(64,activation='relu'))
    #output layer
    model.add(keras.layers.Dense(10,activation='softmax'))


    return model

def predict(model,X):
    #change axis to 4
    X = X[np.newaxis,...]
    #predict label
    prediction = model.predict(X)
    #get highest prob
    prediction = np.argmax(prediction,axis=1)

    return prediction


if __name__ == '__main__':

    #creat train validation test sets
    X_train,X_validation,X_test,Y_train,Y_validation,Y_test = prepare_datasets(0.25,0.2)
    #creat cnn model
    model = build_network((X_train.shape[1],X_train.shape[2],X_train.shape[3]))
    #compile the build_network
    optimizer = keras.optimizers.Adam(learning_rate=0.0001)
    model.compile(
                optimizer = optimizer,
                loss = 'categorical_crossentropy',
                metrics = ['accuracy'])

    #train the network
    model.fit(X_train,Y_train,validation_data=(X_validation,Y_validation),batch_size=32,epochs = 40)

    #evaluate cnn on the test set
    error , accuracy = model.evaluate(X_test,Y_test, verbose=1)
    print('accuracy: ',accuracy)

    #prediction
    X = X_test[0]
    Y = Y_test[0]
    print(predict(model,X))

    model.save('model.h5')
