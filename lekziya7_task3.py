import math
def make_operation():
    operation1 = "+"
    operation2 = "-"
    opr = input("Input operation +|- : ")
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    if opr == operation1:
        print(a+b)
    elif opr == operation2:
        print(a-b)
make_operation()