ofw = open("1.txt", "w+")
a = 1
l = str(a)
print("меня запустили " + l + " раз")
a += 1
readfile = open("1.txt", "r")
resultatsrf = readfile.read()
print(resultatsrf,file=ofw)

