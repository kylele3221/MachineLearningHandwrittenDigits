import tensorflow as tf
import matplotlib.pyplot as plt


mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

for i in range(5):
    plt.imshow(x_train[i])
    plt.show()


