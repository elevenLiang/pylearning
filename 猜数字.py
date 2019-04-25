#coding:utf-8
import random
x = 1
y = 100
num = random.randint(1,100)
while 1:
    print(x,"-",y)
    new_num = input("请猜一个数字：")
    a = int(new_num)
    if a != num and a > num:
        y = a
    elif a != num and a < num:
        x = a
    if a == num:
        print("bingo!!!")
        break
    else:
        print("你是猪吗！！")
#        print(num)