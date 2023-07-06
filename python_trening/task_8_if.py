num = 0
if num >= 0:
    print("Число больше или равно 0")
else:
    print("Число отрицательное")



str_1 = "test"
str_2 = "test1"
if str_1 in str_2:
    print("Да")
else:
    print("Нет")

num_float = 3.4
if num_float > 0:
    print("Положительное число")
elif num_float == 0:
    print("Ноль")
else:
    print("Число отрицательное")

num = 0
permit_print = True
if num > 0 and permit_print:
    print("num - положительное число")
elif not permit_print:
    print("печать запрещена")








def student_rang(year_of_study):
    if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
        print("Вы - бакалавр")
    elif year_of_study in range(5, 7):
        print("Вы - магистрант")
    elif year_of_study in range(7, 10):
        print("Вы - аспирант")
    else:
        print("Введите корректный год обучения")
student_rang(2)









def number(chislo):
    if chislo > art_1 or chislo < art_2:
        print("-")
    else:
        print("+")
art_1 = 100
art_2 = -100
number(10)