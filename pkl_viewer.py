import cPickle 
import gzip
import matplotlib.cm as cm
import matplotlib.pyplot as plt

f = gzip.open('mnist.pkl.gz', 'rb')
training_data, validation_data, test_data = cPickle.load(f)

train_x, train_y = training_data
for i in range(100,97,-1):
    plt.imshow(train_x[i].reshape((28,28)), cmap = cm.Greys_r)
    plt.show()
f.close()