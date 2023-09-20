# -*- coding: utf-8 -*-
"""
Напишите программу для расчета индекса массы тела (body mass index – 
BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы 
используете одну из приведенных ниже формул для определения индекса.
BMI = вес/рост**2 
"""
weight = input()
height = input()


#Ваш кол
def getBMI(w_, h_):
    try:
        w, h = float(w_), float(h_)
    except ValueError:
        print('Error: Parameters are not numbers!')
        raise Exception
    if w <= 0 or h <= 0:
        print('Error: Parameters should be positive numbers!')
        raise Exception
    return w/h**2

print(getBMI(weight, height))
