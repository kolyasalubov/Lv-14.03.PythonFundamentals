class Human:
    def __init__(self):
        None

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    w = Woman()
    m = Man()
    
    people = [m, w]
    
    return people
    