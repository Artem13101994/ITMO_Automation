# task_2
def random(a, b):
    if a > b:
        print(a)
    else:
        print(b)
random(2, 3)



# task_3
a = 11
b = 10
c = a + b
d = a - b
e = b + a
f = b - a
if c > 135 or c < -135 or d > 135 or d < -135 or d > 135 or d < -135 or e > 135 or e < -135:
    print("yes")
else:
    print("no")





# task_4
def seasons(month):
    if month in range (3, 6):
        print("Spring")
    elif month in range (6, 9):
        print("Summer")
    elif month in range (9, 12):
        print("Autumn")
    elif month == 12 or month == 1 or month == 2:
        print("Winter")
    else:
        print("incorrect month")
seasons(3)
seasons(6)
seasons(9)
seasons(1)




# task_5
def fun(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")
fun(9, 13, 14)
fun(11, 12, 13)










# task_6
type_int = (12, -4, -1, 4, 6)
for elem in type_int:
    if elem > 0:
        print(elem)











# task_7
def days(y, m):
    how_mach = y * 348 + m * 29
    print(how_mach)
days(21, 5)
# 348 - Колво дней в году, если в месяце 29 дней
