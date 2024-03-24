import tensorflow as tf

class NeuralNet(tf.keras.Model):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = tf.keras.layers.Dense(hidden_size, input_shape=(input_size,))
        self.l2 = tf.keras.layers.Dense(hidden_size)
        self.l3 = tf.keras.layers.Dense(num_classes)

        self.relu = tf.keras.activations.relu

    def call(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)

        return out