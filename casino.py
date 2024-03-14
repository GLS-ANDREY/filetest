import time, os, random
print("Здравствуйте! У вас 10 монет.")
my_bank = 10

vibor_chisla = input("Выберите одно число от 1 до 6 (включительно) - ")
while vibor_chisla.isnumeric() == False or int(vibor_chisla) >= 7 or int(vibor_chisla) <= 0:
    vibor_chisla = input("Вы выбрали неправильное число. Ещё раз выберите одно число от 1 до 6 (включительно) - ")

vibor_stavki = input("Сделайте вашу ставку - ")
while vibor_stavki.isnumeric() == False or int(vibor_stavki) >= 11 or int(vibor_stavki) <= 0:
    if vibor_stavki.isnumeric() == False:
        vibor_stavki = input("Нужно писать число. Сделайте ставку ещё раз - ")
        continue
    if int(vibor_stavki) >= 11:
        vibor_stavki = input("Вы поставили число больше вашего баланса. Сделайте ставку ещё раз - ")
    if int(vibor_stavki) <= 0:
        vibor_stavki = input("Вы поставили число меньше 1. Сделайте ставку ещё раз - ")

kubik = random.randint(6, 6)
kubiks = str(kubik)
print("Выпало " + kubiks)
if kubiks == vibor_chisla:
    print("Поздравляю! Вы выйграли!")
    my_bank *= int(vibor_stavki)
    print("У вас осталось " + str(my_bank) + " монет")
else:
    print("К сожалению... Вы проиграли")
    my_bank -= int(vibor_stavki)
    print("У вас осталось " + str(my_bank) + " монет")