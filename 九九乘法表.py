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
def jiujiu():
    '''
    九九乘法表
    :return:None
    '''
    for i in range(1,10):
        print_line(i)

jiujiu()
