'''
写一个程序来管理登陆系统的用户信息：登陆名和密码。登陆用户账号建立后，已存在的用户可以用登陆名和密码重返系统，
新用户不能用别人的用户名建立用户。
'''
user_dic = {'zhangsan':123,'lisi':'abc'}

def user_reg(uname,passwd):
    usernames = user_dic.keys()
    if uname in usernames:
        print("用户已存在，请重新输入")
    else:
        print("注册成功")
        user_dic[uname] = passwd


#user_reg('lisi',123456)

def user_log(uname,passwd):
    usernames = user_dic.keys()
    if uname not in usernames:
        print("你猪啊，账号都记不住")
    elif passwd != user_dic[uname]:
        print("猪，密码这就给忘了啊")
    else:
        print('欢迎回来！')
user_log('wangwu','123')
print(user_dic)