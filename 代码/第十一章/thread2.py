
from time import ctime
import time
import threading

def test1():
    for i in range(3):
        print("this is test1 {}".format(ctime()))
        time.sleep(1)

def test2():
    for i in range(3):
        print("this is test2 {}".format(ctime()))
        time.sleep(1)

threads = []
t1 = threading.Thread(target=test1)
threads.append(t1)
t2 = threading.Thread(target=test2)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print("done {}".format(ctime()))