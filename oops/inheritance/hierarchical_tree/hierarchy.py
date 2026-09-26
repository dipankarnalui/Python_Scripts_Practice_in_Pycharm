class A():
    pass
class B(A):
    pass
class C(A):
    pass

class D(B):
    pass
class E(B):
    pass

#       A
#      / \
#     B   C
#    / \
#   D   E
