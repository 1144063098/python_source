class Person:
     __instance = None
     __init = False
     def __new__(cls, *args, **kwargs):
         if cls.__instance == None:
             cls.__instance=object.__new__(cls)
         return  cls.__instance
     def __init__(self,name,age):
         if not self.__init:
             self.name= name
             self.age = age
             self.__init=True

p1 = Person("张三",18)
p2 = Person("李四",20)
print(p1.name)
print(p2.name)




