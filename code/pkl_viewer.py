import cPickle 
import gzip
from time import sleep
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from random import randint
import menu

def view():
    plt.ion()
    file=gzip.open('mnist.pkl.gz','rb')
    training_data,validation_data,test_data=cPickle.load(file)
    train_x,train_y=test_data
    global number
    number=randint(0,10000)
    plt.ion()
    plt.imshow(train_x[number].reshape((28,28)),cmap=cm.Greys_r)
    plt.show()
    plt.pause(0.001) 
    sleep(3)
    plt.close()
    file.close()

def number_return():
    return number