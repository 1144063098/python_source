a = [{"name":"zhangsan","age":18},{"name":"lisi","age":20},{"name":"wangwu","age":30}]
a.sort(key = lambda x:x["age"])
print(a)