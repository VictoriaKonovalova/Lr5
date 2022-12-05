#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    x = float(input("Value of x? "))
    if x < 50:
        z = 0.3 * x
    elif x < 75:
        z = 0.5 * x
    elif x < 90:
        z = 0.65 * x
    else:
        z = (0.7 * x) + 20
    print("Salary: ", z)
