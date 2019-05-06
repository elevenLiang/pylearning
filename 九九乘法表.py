#coding:utf-8

def print_line(line_num):
    '''
    打印一行九九乘法表
    :param line_num:
    :return: None
    '''
    for i in range(1,line_num + 1):
        print('%s * %s = '%(i,line_num),i * line_num,end=" ")
    print()
    return None

def dengyao(space_num):
    '''
    打印空格，变成等腰三角形状
    :param space_num:
    :return: None
    '''
    print(" " * space_num * 5 , end=" ")
    return None

def jiujiu():
    '''
    九九乘法表
    等腰打印
    :return:None
    '''
    for o in range(1,10):
        dengyao(9 - o)
        print_line(o)
    return None
jiujiu()
