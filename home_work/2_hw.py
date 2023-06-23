def task_1(a, b, c, d, e) -> str:
    return a+b
    add(4, 8.15, c="kaef", d=[16,23,42], e=1==1)
a: int=4
b: float=8.15
c: str="kaef"
d: list=[16,23,42]
e: bool=1==1
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(task_1(a, b, c, d, e))

def task_2(a=[1, 2, 3, 5, 8, 13, 21]) -> list:
    return a[0:3]
print (task_2())

Task_3 = pow(7, 2)
print(Task_3)