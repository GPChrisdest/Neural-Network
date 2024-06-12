import cPickle 
import gzip
from time import sleep
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from random import randint
import menu

def view():
    plt.ion()
    file = gzip.open('mnist.pkl.gz', 'rb')
    training_data, validation_data, test_data = cPickle.load(file)

    train_x, train_y = test_data
    number =randint(0,10000)
    while True:
        plt.ion()
        plt.imshow(train_x[number].reshape((28,28)), cmap = cm.Greys_r)
        plt.show()
        plt.pause(0.001) 
        sleep(3)
        plt.close()
        print("Do you want to select this photo?")
        print("1. Yes")
        print("2. No")
        try:
            x = int(input(">>>"))
            if x == 1:
                break
            elif x==2:
                number = randint(0,10000)
                continue
        except NameError:
            print("Please enter a valid choice!")
            sleep(2)
            continue
    file.close()
    return number