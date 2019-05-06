#coding:utf-8
'''
    九九乘法表
    version 1.0
'''
for i in range(1,10):   #控制外循环，1-9；
    for o in range(1,i + 1):    #控制内循环，每行最多打印几个由i控制；
        print('%s * %s = '%(o,i),i * o,end=" ")
    print()
print('==' * 55)
def jiujiu():
    '''
    九九乘法表
    version 1.1
    函数封装
    :return:None
    '''
    for i in range(1,10):
        for o in range(1,i + 1):
            print('%s * %s = '%(o,i),i * o,end=" ")
        print()
    return None

jiujiu()

print('==' * 55)

def print_line(line_num):
    '''
    每次只打印一行九九乘法表
    version 2.0
    :param line_num:
    :return: None
    '''
    for i in range(1,line_num + 1):
        print('%s * %s = '%(i,line_num),i * line_num,end=" ")
    print()
    return None
def print_jiujiu():
    '''
    控制九九乘法表行数
    version 2.0
    :return:None
    '''
    for o in range(1,10):
        print_line(o)
    return None

print_jiujiu()
