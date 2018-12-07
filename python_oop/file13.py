
ls=["唐诗","宋词","元曲"]
f = open("a.txt","w+")
f.writelines("tfgykuhlijlok")
f.seek(0)
for line in f:
    print(line)
f.close()



