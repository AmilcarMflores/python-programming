class A:
  def __init__(self, factor):
    self.__factor = factor
    
  def op1(self):
    print("Op1 con factor {}...".format(self.__factor))
    
class B(A):
  def op2(self, factor):
    self.__factor = factor
    print("Op2 con factor {}...".format(self.__factor))
    
obj = B(100)
obj.op1() # Op1 con factor 100...
obj.op2(42) # Op2 con factor 42...
obj.op1() # Op1 con factor 100...