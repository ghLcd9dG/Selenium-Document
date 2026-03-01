
from time import ctime
import time

def test1():
    for i in range(3):
        print("this is test1 {}".format(ctime()))
        time.sleep(1)

def test2():
    for i in range(3):
        print("this is test2 {}".format(ctime()))
        time.sleep(1)

if __name__ == '__main__':
    test1()
    test2()
    print("done {}".format(ctime()))