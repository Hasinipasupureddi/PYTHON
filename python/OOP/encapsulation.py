class Grandfather():
    def __init__(self):
        self.a=10
        self._b=20
        self.__c=30
    def _fun1(self):
        print("this is our house")
    def __fun2(self):
        print("this is my farm house")
class father(Grandfather):
    def fun3(self):
        print("i have 20cr")
ob=Grandfather()
ob._Grandfather__fun2()
ob1=father()
ob1._fun1()
print(ob1._b)