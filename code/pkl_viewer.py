import cPickle 
import gzip
import matplotlib.cm as cm
import matplotlib.pyplot as plt

def view():
    f = gzip.open('mnist.pkl.gz', 'rb')
    training_data, validation_data, test_data = cPickle.load(f)

    train_x, train_y = test_data
    for i in range(0,10000,1):
        plt.imshow(train_x[i].reshape((28,28)), cmap = cm.Greys_r)
        plt.show()
        print("Select this photo?")
        print("1. Yes")
        print("2. No")
        x = input()
        if x == 1:
            break
        else:
            continue
    f.close()
    return i