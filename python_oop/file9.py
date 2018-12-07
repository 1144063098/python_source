def leichen(a):
    if a==1 or a==0:
        return 1
    else:
        return a*leichen(a-1)
sum=0
i=0
while i<=10:
    sum=sum+leichen(i)
    i=i+1
print(sum)


