#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Составить программу, выясняющую делится ли натуральное число нацело на
натуральное число .
'''


if __name__ == '__main__':
    x = int(input("Введите максимальное натуральное число: "))
    y = int(input("Введите натуральное число на которое делить: "))
    if x % y == 0:
        print("Yes")
    else:
        print("No")
