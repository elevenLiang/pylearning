#设计一个验证用户密码的程序，用户只能输入3次机会，如果输入内容带“*”则不计次数

code = "root123"
count = 0
while count < 3:
    input_code = input("请输入您的密码：")
    if input_code == code:
        print("Bingo!")
        # count += 1
        break
    # elif input_code.find('*') != -1:
    #     continue
    elif '*' in input_code:
        print("密码中不能包含*号")
    else:
        print("你猪啊！")
        count += 1
        if count != 3:
            print("还有{}次机会".format(3 - count))
        else:
            print("已经输错超过3次了！")
