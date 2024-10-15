import tensorflow as tf
import matplotlib.pyplot as plt


# Get mnist dataset
mnist = tf.keras.datasets.mnist

# Splits the mnist dataset into two datatsets.  One for training and one for testing 
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Shows the first five images in the training set
for i in range(5):
    plt.imshow(x_train[i])
    plt.show()


