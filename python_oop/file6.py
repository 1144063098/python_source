class Person:
    def __init__(self,name,age):
       self.__name=name
       self.__age=age
    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age
    def __del__(self):
        print("对象要被删除了")


p = Person("张三",19)
print(p.getAge())