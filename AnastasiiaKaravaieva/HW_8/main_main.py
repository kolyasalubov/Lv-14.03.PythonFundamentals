
import sys
sys.path.append('c:\\Users\\Анастасия\\Desktop\\second\\Lv-14.03.PythonFundamentals\\AnastasiiaKaravaieva\\HW_8\\models')
sys.path.append('c:\\Users\\Анастасия\\Desktop\\second\\Lv-14.03.PythonFundamentals\\AnastasiiaKaravaieva\\HW_8\\utils')

from utils import *
from  models import *

print(list(filter(lambda str: not ("__" in str), dir()))) 