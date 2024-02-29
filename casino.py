import time,os,random
print("Здравствуйте! У вас 10 монет.")
time.sleep(1)
while True:
    vibor = input("Выберите одно числа от 1 до 6 (включительно)")
    vibor_proverka = vibor.isnumeric()
    if vibor_proverka == True:
        vibor_int = int(vibor)
    if vibor_proverka == False or vibor_int > 6 or vibor_int < 1:
        input("Вы сделали не правильную ставку. Ещё раз выберите одно число от 1 до 6 (включительно)")
    if vibor_int < 6 and vibor_int > 1:
        break
    vibor_str = str(vibor)
    vibor_str = vibor
kubik = random.randint(1,6)
kubiks = str(kubik)
print("Выпало " + kubiks)