from circle import Circle
import pygame
from datetime import datetime
import random
from point import Point

class Voronoi:
    noCircles = 10
    scale = 5

    def __init__(self):
        self.circles = []
        random.seed(datetime.now())
        for index in range(self.noCircles):
            center = Point(random.randint(0,100*Voronoi.scale),random.randint(0,100*Voronoi.scale))
            self.circles.append(Circle(center))

    def draw(self):
        background = (255,255,255)        
        (width, height) = (100*Voronoi.scale, 100*Voronoi.scale)
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Voronoi')
        screen.fill(background)

        blue = (0,0,255)
        P = []
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            screen.fill(background)
            for circle in self.circles:
                circle.increment_radius()
                circle.draw(screen) 
            for i in range(len(self.circles)):
                for j in range(i+1,len(self.circles)):
                    p = self.circles[i]
                    q = self.circles[j]
                    points = Circle.is_intersection(p,q)     
                    for point in points:
                        inside = False
                        for k in range(len(self.circles)):
                            if k != i and k != j and self.circles[k].is_inside(point):
                                inside = True
                        if not inside:        
                            P.append(point)
            for point in P:        
                point.draw(screen,blue)

            pygame.display.update()    
            pygame.time.delay(50)  
