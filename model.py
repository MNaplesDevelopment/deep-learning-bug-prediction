from __future__ import absolute_import, division, print_function
import tensorflow as tf
from tensorflow import keras
import numpy as np
print(tf.__version__)

#Convert lists into numpy arrays
testLabel_np = np.asarray(trainLabel, np.float32)
trainLabel_np = np.asarray(testLabel, np.float32)
testData_np = np.asarray(trainData, np.float32)
trainData_np = np.asarray(testData, np.float32)

print("Training set: {}".format(trainData_np.shape))
print("Testing set: {}".format(testData_np.shape))
#Training set has 1323 examples with 17 features each.
#Teststingg set has 823 examples with 17 features each.

#Normalize the data value
mean = trainData_np.mean(axis=0)
std = trainData_np.std(axis=0)
trainData_np = (trainData_np - mean) / std
testData_np = (testData_np - mean) / std

#Construct a neural network
def build_model():
    model = keras.Sequential([
        keras.layers.Dense(16, activation=tf.nn.relu,
                           input_shape=(testData_np.shape[1],)),
        keras.layers.Dense(16, activation=tf.nn.relu),
        keras.layers.Dense(1)
    ])
    
    optimizer = tf.train.RMSPropOptimizer(0.001)
    model.compile(loss='mse',
                 optimizer=optimizer,
                 metrics=['mae'])
    return model

model = build_model()
model.summary()

#Set stuff up
import matplotlib.pyplot as plt

def plot_history(history):
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error')
    plt.plot(history.epoch, np.array(history.history['mean_absolute_error']),
            label='Train loss')
    plt.plot(history.epoch, np.array(history.history['val_mean_absolute_error']),
            label='Val loss')
    plt.legend()
    plt.ylim([0,5])
    

class PrintDot(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs):
        if epoch %100 == 0: print('')
        print('.', end='')

EPOCHS = 500
model = build_model()
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=20)

#Train the model
history = model.fit(testData_np, testLabel_np, epochs=EPOCHS,
                   validation_split=0.2, verbose=0,
                   callbacks=[early_stop, PrintDot()])
                   
#Plot the train loss vs the validation score
plot_history(history)

[loss, mae] = model.evaluate(trainData_np, trainLabel_np, verbose=0)
print("Testing set Mean Abs Error: {:7.2f}".format(mae))

test_predictions = model.predict(trainData_np).flatten()

plt.scatter(trainLabel_np, test_predictions)
plt.xlabel('True values')
plt.ylabel('Predictions')
plt.axis('equal')
plt.xlim(plt.xlim())
plt.ylim(plt.ylim())
_ = plt.plot([-100,100],[-100,100])
#Plots how the model is fitting the data

error = test_predictions - trainLabel_np
plt.hist(error, bins = 50)
plt.xlabel("Prediction Error")
_ = plt.ylabel("Count")
