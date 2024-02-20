import os

r = open("1.txt", "r")
p = r.read()
r.close()

if p == "":
    otvetp = input("Привет, до тебя здесь никого не было, ты кто?")
    k = open("2.txt", "a")
    print(otvetp,file=k)
    k.close()


if p != "":
    input("Привет, до тебя здесь был " + p + ", ты кто?")
