import time,os,random
print("Здравствуйте! У вас 10 монет.")
time.sleep(1)
vibor_int = 3
while True:
    if vibor_int < 6 and vibor_int > 1:
        vibor = input("Выберите одно число от 1 до 6 (включительно) - ")
        vibor_proverka = vibor.isnumeric()
        if vibor_proverka == True:
            vibor_int = int(vibor)
    if vibor_int > 6 or vibor_int < 1 or vibor_proverka == False:
        vibor_false = input("Вы сделали не правильную ставку. Ещё раз выберите одно число от 1 до 6 (включительно) - ")
        vibor_proverka_false = vibor_false.isnumeric()
        if vibor_proverka_false == True:
            vibor_false = int(vibor_false)
    if vibor_int <= 6 and vibor_int >= 1 or vibor_false <= 6 and vibor_false:
        break
kubik = random.randint(1,6)
kubiks = str(kubik)
print("Выпало " + kubiks)
