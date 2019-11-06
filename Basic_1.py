import keyword
import sys
import math

#id(Object): 对象的地址
#type(Object):返回对象类型
a = 10
b = 1
c = a
print(id(c))

c = 100
print(id(c))
print(type(c))

def NumTest():
    s = input("enter an integer:")
    try:
        i = int(s)
        print("valid interger entered:",i)
    except ValueError as err:
        print(err)

def equal_float(a,b):
    return abs(a -b) <= sys.float_info.epsilon

def strtest():
    s = "The waxwork man"
    s = s[:12]+"wo"+s[12:]
    return s

#  在字符串中查找
def finInStr(a,b):
    

if __name__ == "__main__":
    print(equal_float(1.0,1.000001))
    print(strtest())