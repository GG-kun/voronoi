import pygame
import math
from point import Point

class Circle:
    scale = 5  

    def __init__(self,center, radius=0):        
        self.center = center
        self.radius = radius
        self.set_max_radius()

    def set_radius(self,radius):
        self.radius = radius

    def increment_radius(self):        
        if self.radius < self.maxRadius:
            self.radius += 1

    def draw(self,screen):
        black = (0,0,0)        
        red = (255,0,0)
        pygame.draw.circle(screen,black,self.center,self.radius,1)
        self.center.draw(screen,red)

    def set_max_radius(self):
        ca = self.center[0]
        if ca < 50*Circle.scale:
            ca = Circle.scale*100 - ca
        co = self.center[1]
        if co < 50*Circle.scale:
            co = Circle.scale*100 - co
        h = math.sqrt(ca*ca + co*co)
        self.maxRadius = h

    def is_inside(self, point):
        x = point[0] - self.center[0]
        y = point[1] - self.center[1]
        return math.sqrt(x*x + y*y) < self.radius

    @staticmethod
    def is_intersection(p,q):
        D = p.center - q.center
        d = D.magnitude()

        if (d > p.radius + q.radius):
            return []

        h = math.sqrt(p.radius*q.radius - d*d/4)
        x0 = p.center[0]
        y0 = p.center[1]
        x1 = q.center[0]
        y1 = q.center[1]
        P0 = p.center
        P1 = q.center
        P2 = P0 + ((P1-P0)/2)
        fx = h*(y0-y1) / d
        fy = h*(x1-x0) / d

        return [Point(P2[0]+fx,P2[1]+fy), Point(P2[0]-fx,P2[1]-fy)] 