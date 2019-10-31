import keyword
import sys

#保留关键字
print("Hello,Python")
# 注释方式

# 行与缩进，上下保持缩进一致

if True:
    print("True")
else:
    print("False")

# 多行语句
item_one = 'one'
item_two = 'two'
item_three = 'three'
total = item_one + \
        item_two + \
        item_three

print(total)
# 数字类型：python 中数字有四种类型：整数 int, 布尔型 bool,浮点数 float, 复数 complex.


# 字符串
str = 'Runoob'
print(str) # 输出字符串
print(str[0:-1]) # 输出字符串 0 : size -1
print(str[0])    # 输出字符  0
print(str[2:5])  # 输出第三个到第五个
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

#空行：函数之间或类的方法之间用空行分隔