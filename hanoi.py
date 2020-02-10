# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:57:41 2020

@author: Jilin Men
"""
def hanoi(n, a, b, c):
    if n==1:
        print(a , '-->', c)
    else:
        hanoi(n-1, a, c, b)
        print(a, '-->', c)
        hanoi(n-1, b, a, c)


hanoi(3, 'A', 'B', 'C')
