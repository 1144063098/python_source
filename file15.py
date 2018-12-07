def digui(n):
    if n==1 or n==0:
        return 1
    else:
        return  digui(n-1)*n
sum = digui(3)
print(sum)
