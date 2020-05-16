import pygame
import math

class Point:    

    def __init__(self,x=0,y=0):
        self.coord = (x,y)

    def draw(self, screen,color):
        pygame.draw.circle(screen,color,(int(self.coord[0]),int(self.coord[1])),3) 

    def __getitem__(self,number):
        return self.coord[number]       

    def __len__(self):
        return len(self.coord)

    def __add__(self,other):
        return Point(self[0]+other[0], self[1]+other[1])

    def __sub__(self,other):
        return Point(self[0]-other[0], self[1]-other[1])

    def __mul__(self,scalar):
        return Point(self[0]*scalar,self[1]*scalar)

    def __truediv__(self,scalar):
        return Point(self[0]/scalar,self[1]/scalar)

    def __repr__(self):
        return "(" + str(self[0]) + "," + str(self[1]) + ")"

    def __lt__(self, other):
        if self[0] < other[0]:
            return self 
        else:
            return other    
    
    def magnitude(self):
        return math.sqrt(self[0]*self[0] + self[1]*self[1])