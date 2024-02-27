import time,os,random
print("Здравствуйте! У вас 10 монет.")
time.sleep(1)
vibor = input("Выберите два числа от 1 до 6 (включительно)")
stavka = input("Сколько вы поставите монет на эти числа?")
kubik = random.randint(1,6)
kubiks = str(kubik)
print("Выпало " + kubiks)