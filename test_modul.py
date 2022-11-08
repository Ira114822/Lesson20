# 1)
import some_modul

# 2)
# from some_modul import __a, __b, A, B

# 3)
# from some_modul import __a as alfa
#
# a = alfa

# 4)использует инкапсуляцию(инкапсуляция на уровне модуля)
from some_modul import *
from some_modul import *
from some1 import *
from some2 import *
a = test_a()