import math
def lines(coordlist):
    """
    koordináta listából éllistát csinál. 
    [(10,10), (30,30), (50,30)] ->
    [((10,10), (30,30)), ((30,30), (50,30)), ((50,30), (10,10))] 
    """
    num = len(coordlist)
    edges = [(coordlist[i],coordlist[i+1]) for i in range(num-1)]
    edges.append((coordlist[num-1], coordlist[0]))
    return edges

def to_polar(center, point):
    """
    (cx,cy) középpontú polár koordinátákra vált
    """
    cx,cy = center
    x,y = point
    dx, dy = x-cx, y-cy
    a = math.atan(dx/dy) if dy != 0 else math.pi/2 if dx > 0 else -math.pi/2
    r = math.sqrt(dx*dx + dy*dy)
    if dy < 0 : a += math.pi 
    if a < 0 : a += 2*math.pi
    return (a,r)

def from_polar(center, ppoint):
    """ (cx,cy) középpont körüli polárkoordinátákból x,y koordinátákra vált """
    cx,cy = center
    a,r = ppoint
    return (r * math.sin(a) + cx, r * math.cos(a) + cy) 

def fok(ppoint):
    return (ppoint[0]*180/math.pi, ppoint[1])

def trapezok(polygon, center, maxlight):
    """ kiszűri a nemlátható éleket  és létrehozza az árnyéktrapézokat
        x2 > x1 kivéve ha "túlfordul" vagyis átlép a 360 fokos határon
        (ez akkor fordul elő ha x1-x2 > pi)
    """
    cx, cy = center
    quads = []
    for p1, p2 in lines(polygon):
        pp1, pp2 = to_polar(center, p1), to_polar(center, p2)
        a1, a2 = pp1[0], pp2[0]
        l = a2 - a1
        if (l>0 and l<math.pi) or l<-math.pi: # látható
            middle = (a1+a2)/2 if l>-math.pi else (a1+a2)/2+math.pi
            tpoly = (pp1, pp2, (a2,maxlight), (middle, maxlight), (a1,maxlight) )
            tdek = list(from_polar(center, p) for p in tpoly)
            quads.append(tdek)
    return(quads)


if __name__ == "__main__":
    center = 300,300
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
        pol = to_polar(center,p) 
        orig = list(round(x,10) for x in from_polar(center,pol))
        print(p,"->", (pol[0]*180/math.pi, pol[1] ),  "->", orig)
        assert(list(p) == orig) 
        print("-----------------------")
    print()

    print (trapezok(pontok, center, 200))


    



