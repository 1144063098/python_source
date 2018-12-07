import types
class Person:
    pass
def run(self):
    print("—--跑---")
p1=Person()
p1.run=types.MethodType(run,p1)
p1.run()