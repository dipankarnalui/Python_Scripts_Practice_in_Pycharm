'''

                       C:
                       |--------> main.py (we are HERE)
                      apps
                       |
             ----------------------
            |                      |
           desk                   web
            |                      |
    -----------------            omega.py
   |                 |           ---------
  alpha.py        beta.py        def fun3():
  --------        -------            print("Fun3")
  def fun1():     def fun2():
     print("fun1")    print("fun2")

# we need to call fun1,fun2 & fun3 within main.py
from apps import * 

desk.alpha.fun1()
desk.bet1.fun2()
web.omega.fun3()

# we need to call fun1 & fun2 within main.py
from apps.desk import *

alpha.fun1()
beta.fun2()

# we need to load a lib & call fun1() within main.py
import apps.desk.alpha

apps.desk.alpha.fun1()

'''