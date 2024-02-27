import os

if os.path.exists("2.txt") == False:
    k = open("2.txt", "w+")
    print("никто", file=k, end="")
    k.close()

r = open("2.txt", "r")
p = r.read()
r.close()

if p == "" or p == "никто" or p == "Никто" or p == "nikto" or p == "Nikto":
    otvetp = input("Привет, до тебя здесь никого не было, ты кто?")
    k = open("2.txt", "w+")
    print(otvetp, file=k, end="")
    k.close()
else:
    otvet = input("Привет, до тебя здесь был " + p + ", ты кто?")
    k = open("2.txt", "w+")
    print(otvet, file=k, end="")
    k.close()