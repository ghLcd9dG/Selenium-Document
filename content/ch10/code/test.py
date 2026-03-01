import HTMLTestRunner
import unittest

directory=r"C:\Users\xuyichenmo\OneDrive\Documents\SELENIUM\第十章"

def createsuite():
    test_suit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(directory,pattern='book_unittest.py',top_level_dir=None)
    counter=0
    print(discover)
    for i in discover:
        counter+=1
        print("已发现{}个测试实例需要执行".format(counter))
        for j in i:
            test_suit.addTests(j)
    return test_suit

def main():

    filename="E:\\result.html"
    f=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='测试报告',description='实例执行情况：')
    runner.run(createsuite())
    f.close()

if __name__ == '__main__':
    main()
