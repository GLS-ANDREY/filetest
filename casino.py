import time, os, random

if os.path.exists("zapis_casino_file") == False:
    zapis_casino = open("zapis_casino_file", "w+")
    print(10,file=zapis_casino,end="")
    zapis_casino.close()

read_casino = open("zapis_casino_file", "r")
read_casino_bank = read_casino.read()
print("Здравствуйте! У вас " + read_casino_bank + " монет.")
time.sleep(0.4)
read_casino.close()
my_bank = int(read_casino_bank)

vibor_chisla = input("Выберите одно число от 1 до 6 (включительно) - ")
while vibor_chisla.isnumeric() == False or int(vibor_chisla) > 6 or int(vibor_chisla) < 1:
    vibor_chisla = input("Вы выбрали неправильное число. Ещё раз выберите одно число от 1 до 6 (включительно) - ")

vibor_stavki = input("Сделайте вашу ставку - ")
if vibor_stavki.lower() == "мани":
    my_bank = 1000000000
    print("Ваш Прадед всегда знал что вы догадливый парень, вам по наследству от него пришел 1 миллиард монет")
    time.sleep(0.7)
while vibor_stavki.isnumeric() == False or int(vibor_stavki) >= my_bank+1 or int(vibor_stavki) <= 0:
    if vibor_stavki.isnumeric() == False:
        vibor_stavki = input("Нужно писать число. Сделайте ставку ещё раз - ")
        continue
    if int(vibor_stavki) >= my_bank+1:
        vibor_stavki = input("Вы поставили число больше вашего баланса. Сделайте ставку ещё раз - ")
    if int(vibor_stavki) <= 0:
        vibor_stavki = input("Вы поставили число меньше 1. Сделайте ставку ещё раз - ")

kubik = random.randint(1, 6)
kubiks = str(kubik)
print("Выпало " + kubiks)
time.sleep(0.5)
if kubiks == vibor_chisla:
    print("Поздравляю! Вы выйграли!")
    my_bank -= int(vibor_stavki)
    my_bankwin = int(vibor_stavki) * 6
    my_bank += my_bankwin
    time.sleep(0.5)
    print("Теперь у вас " + str(my_bank) + " монет")
else:
    print("К сожалению... Вы проиграли")
    my_bank -= int(vibor_stavki)
    time.sleep(0.5)
    print("У вас осталось " + str(my_bank) + " монет")

zapis_casino = open("zapis_casino_file", "w+")
print(my_bank, file=zapis_casino,end="")
zapis_casino.close()