import os
if os.path.exists("1.txt") == False:
    k = open("1.txt", "w+")
    print(1,file=k,end="")
    k.close()

r = open("1.txt", "r")
p = r.read()
a = p
r.close()

l = str(a)
print("меня запустили " + l + " раз")
u = int(a)
a = u
a += 1

o = open("1.txt", "w+")
print(a,file=o,end="")
o.close()