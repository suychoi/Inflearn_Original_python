import sys
import inspect

def mod2_test1():
    print("Module2 -> TEST 1")
    print('Path : ', inspect.getfile(inspect.currentframe()))

def mod2_test2():
    print("Module2 -> TEST 2")
    print('Path : ', inspect.getfile(inspect.currentframe()))