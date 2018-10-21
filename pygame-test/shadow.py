""" Shadow and visibility library """

import math

def polar(point):
    """
    polár koordinátákra vált
    """
    dx,dy = point
    a = math.atan(dx/dy) if dy != 0 else math.pi/2 if dx > 0 else -math.pi/2
    r = math.sqrt(dx*dx + dy*dy)
    if dy < 0 : a += math.pi 
    if a < 0 : a += 2*math.pi
    return (a,r)

def cartesian(ppoint):
    """ polárkoordinátákból x,y koordinátákra vált """
    a,r = ppoint
    return (r * math.sin(a), r * math.cos(a)) 

def fok(ppoint):
    return (ppoint[0]*180/math.pi, ppoint[1])

def points2edges(coordlist):
    """
    convert coordinate list to edge list (making tuples and repeat last point)
    [(10,10), (30,30), (50,30)] ->
    [((10,10), (30,30)), ((30,30), (50,30)), ((50,30), (10,10))] 
    """
    num = len(coordlist)
    edges = [(coordlist[i],coordlist[i+1]) for i in range(num-1)]
    edges.append((coordlist[num-1], coordlist[0]))
    return edges

class Obstacles:
    """
    Obstacles class. Obstacles can hinder visibility or 
    cast shadow ("visibility" of lightsources) 
    """
    def __init__(self, obstacles = [], source_point = (0,0)):
        """ obstacles: obstacle poligon list
            obstacle poligon: list of vertexes, clocwise
        """
        self.source = source_point
        self.edges = []
        self.add_obstacle(obstacles)

    def add_obstacles(self, obstale_list):
        self.obstacles = obstacle_list
        for o in obstacle_list:
            self.generate_edges(o)

    def generate_edges(self, obstacle):
        """ obstacle: clocwise list of vertices"""
        self.edges.append(point2edges(obstacle))


    def shadows(self, center, maxlight):
        """ kiszűri a nemlátható éleket  és létrehozza az árnyékalakokat
            x2 > x1 kivéve ha "túlfordul" vagyis átlép a 360 fokos határon
            (ez akkor fordul elő ha x1-x2 > pi)
        """
        quads = []
        cx,cy = center
        edgelist = [ ((px1-cx, py1-cy), (px2-cx,py2-cy)) for (px1,py1), (px2,py2) in self.edges]
        for p1, p2 in edgelist:
            pp1, pp2 = polar(p1), polar(p2)
            a1, a2 = pp1[0], pp2[0]
            l = a2 - a1
            if (l>0 and l<math.pi) or l<-math.pi: # látható
                middle = (a1+a2)/2 if l>-math.pi else (a1+a2)/2+math.pi
                tcart = (p1, p2, 
                        cartesian((a2,maxlight)), 
                        cartesian((middle, maxlight)), 
                        cartesian((a1,maxlight)) )
                quads.append(tcart)
        return(quads)



if __name__ == "__main__":
    pontok = [
            (0,0),
            (30,50),
            (170,150),
            (50,200),
            (200,50),
            (400,450),
            (475,410),
            ]

    print('polar test:')
    for p in pontok:
        pol = polar(p) 
        orig = list(round(x,10) for x in cartesian(pol))
        print(p,"->", (pol[0]*180/math.pi, pol[1] ),  "->", orig)
        assert(list(p) == orig) 
        print("-----------------------")
    print()

    print (trapezok(lines(pontok), 200))


    



