import sys
import inspect

def mod1_test1():
    print("Module1 -> TEST 1")
    print('Path : ', inspect.getfile(inspect.currentframe()))

def mod1_test2():
    print("Module1 -> TEST 2")
    print('Path : ', inspect.getfile(inspect.currentframe()))