# import time,os,random
# print("Здравствуйте! У вас 10 монет.")
# time.sleep(1)
# vibor_int = 3
# while True:
#     if vibor_int < 6 and vibor_int > 1:
#         vibor = input("Выберите одно число от 1 до 6 (включительно) - ")
#         vibor_proverka = vibor.isnumeric()
#         if vibor_proverka == True:
#             vibor_int = int(vibor)
#     if vibor_int > 6 or vibor_int < 1 or vibor_proverka == False:
#         vibor_false = input("Вы сделали не правильную ставку. Ещё раз выберите одно число от 1 до 6 (включительно) - ")
#         vibor_proverka_false = vibor_false.isnumeric()
#         if vibor_proverka_false == True:
#             vibor_false = int(vibor_false)
#     if vibor_int <= 6 and vibor_int >= 1 or vibor_false <= 6 and vibor_false:
#         break
# kubik = random.randint(1,6)
# kubiks = str(kubik)
# print("Выпало " + kubiks)

import time,os,random
print("Здравствуйте! У вас 10 монет.")
vibor_chisla = input("Выберите одно число от 1 до 6 (включительно) - ")
while vibor_chisla.isnumeric == False or int(vibor_chisla) >= 6 or int(vibor_chisla) <= 1:
    vibor_chisla = input("Вы сделали не правильную ставку. Ещё раз выберите одно число от 1 до 6 (включительно) - ")
kubik = random.randint(1,6)
kubiks = str(kubik)
print("Выпало " + kubiks)

# импорты
# первый вопрос
# вайл нельзя сделать ответ числом или число больше 6 или меньше 1
#     просить ввести число еще раз
# что то выпало

