a={"name":"张三","age":18,"addr":"长沙"}
s={k:v for k,v in a.items() if k=="age" or k=="addr"}
print(a.get("named",18))

