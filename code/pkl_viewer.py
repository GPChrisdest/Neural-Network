import cPickle 
import gzip
from time import sleep
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from random import randint

def view():
    plt.ion()
    f = gzip.open('mnist.pkl.gz', 'rb')
    training_data, validation_data, test_data = cPickle.load(f)

    train_x, train_y = test_data
    while True:
        plt.ion()
        i=randint(0,10000)
        plt.imshow(train_x[i].reshape((28,28)), cmap = cm.Greys_r)
        plt.show()
        plt.pause(0.001) 
        sleep(3)
        plt.close()
        print("Do you want to select this photo?")
        print("1. Yes")
        print("2. No")
        x = int(input(">>>"))
        try:
            if x == 1:
                break
            elif x==2:
                continue
        except NameError:
            print("Please enter a valid choice!")
            view()
    f.close()
    return i