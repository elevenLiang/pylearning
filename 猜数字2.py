
import random
A = random.randint(1,100)
print(A)
count = 0
while 1:
    num = input("猜猜这个数字是什么")
    if num.isdigit():
        if int(num) == A:
            print("你猜对了，数字为"+str(A))
            break
        elif int(num) > A:
            print("猜错了，数字大于A")
        else:
            print("猜错了，数字小于A")
    else:
        print("叫你输入数字！")
#        break
    count += 1
    if count != 3:
        print("还有{}次机会".format(3 - count))
    else:
        print("lost")
        break
