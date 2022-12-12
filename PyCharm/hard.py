#!\usr\bin\env python3
# -*- coding: utf-8 -*-

import sys
import math

if __name__ == '__main__':
    x = float(input("Value of x? "))
    if x == 0:
        print("Illegal value of x", file=sys.stderr)
        exit(1)
    a = x
    S, n = a, 1
    while math.fabs(a) > EPS:
        a *= ((x ** 2) * (2 * n + 1)) / (((2 * n + 3) ** 2) * (2 * n + 2))
        S += a
        n += 1

print(f"Shi({x})={S}")
