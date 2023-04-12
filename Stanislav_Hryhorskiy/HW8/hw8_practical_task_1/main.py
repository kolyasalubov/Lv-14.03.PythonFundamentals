from utils import *
from models import *

print(list(filter(lambda string: not ("__" in string), dir())))
