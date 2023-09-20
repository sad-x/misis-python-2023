# -*- coding: utf-8 -*-
"""
Разработайте программу, запрашивающую у  пользователя целое четырехзначное число и подсчитывающую сумму составляющих его цифр. Например, если пользователь введет число 3141,
 программа должна вывести 
следующий результат: 3 + 1 + 4 + 1 = 9

@author: Savant
"""
def task4(num_):
    try:
        num = int(num_)
    except ValueError:
        print('input should be int')
        raise
    if len(str(num)) != 4:
        print('input should be 4 symbols long')
        return
    arr = [int(n) for n in list(str(num))]
    return ' + '.join([str(i) for i in arr]) + f' = {sum(arr)}'

myNum = input()
print(task4(myNum))
