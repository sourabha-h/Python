# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 18:57:37 2019

@author: A539647
"""

class Clothing:
    def __init__(self,size,color,cost):
        self.size=size
        self.color=color
        self.cost=cost
    
    def display(self):
        print(self.size);
        print(self.color);
        print(self.cost);
        
A=Clothing(42,"Red",3000)
A.display()
        