# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:34:17 2019

@author: dtunc
"""

import math

class Circle:
    radius = 1.0
    diameter = 0.0
    area = 0.0
    def __init__(self,radius = 1):
        self.radius = radius
        self.calculateDiameter()
        self.calculateArea()
        
        
        
        
    def calculateDiameter(self):
        self.diameter = 2*math.pi*self.radius
        return
    def calculateArea(self):
        self.area = math.pi*self.radius*self.radius
        return
    
    def __setattr__(self,radius,value):
        print("yeni radius geldi")
        self.radius = value
        self.calculateDiameter()
        self.calculateArea()
        return

