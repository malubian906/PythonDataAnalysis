import sys
import turtle
#
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and j != k and i != k:
               print(i,j,k)
# 
a, b = 0, 1
while b < 1000:
    print(b, end=",")
    a, b = b, a+b

###########
var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)

print("Good bye!")
#：while  循环
"""
while  循环使用else 
"""
