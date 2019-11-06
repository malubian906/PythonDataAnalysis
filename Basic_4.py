import sys
import cmath
import math
# 获取参数数值
def get_float(msg,allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print('zero is not allowed')
                x = None
        except ValueError as err:
            print(err)
    return x

def quadratic():
    v1 = None
    v2 = None

    print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")
    a = get_float("enter a:",False)
    b = get_float("enter b:",True)
    c = get_float("enter c:",True)

    discriminant = (b**2)-(4*a*c)
    if discriminant == 0:
        v1 = -(b/(2*a))
    else:
        if discriminant > 0:
            root = math.sqrt(discriminant)
        else:
            root = cmath.sqrt(discriminant)
    f_b = -1*b
    v1 = (f_b + root)/(2*a)
    v2 = (f_b - root)/(2*a)  
    print(v1,v2) 


if __name__ == "__main__":
    quadratic()