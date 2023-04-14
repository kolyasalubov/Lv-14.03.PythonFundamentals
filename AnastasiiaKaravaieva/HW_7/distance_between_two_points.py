import math

def distance(x1, y1, x2, y2):
    distance_x = (x2-x1)**2
    distance_y = (y2 -y1)**2
    d = math.sqrt(distance_x + distance_y)
    return round(d,2)