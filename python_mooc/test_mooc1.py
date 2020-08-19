# -*- coding: UTF-8 -*-

def logging(func):
    def print_fuc(*args,**kwargs):
        print('this is '+func.__name__+'的程序')
        return func(*args,**kwargs)
    return print_fuc

@logging
def deng():
    print("this is 邓宝雷")


@logging
def deng1():
    print("this is 邓宝雷1")

deng()
deng1()