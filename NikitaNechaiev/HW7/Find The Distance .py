def distance(x1, y1, x2, y2):
    dist_count = (x2 - x1)**2 + (y2 - y1)**2
    dist_count = round(dist_count,2)
    return dist_count



print(distance(5,2,4,3))