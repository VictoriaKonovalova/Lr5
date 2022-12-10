#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано натуральное число . Получить все его натуральные делители.

if __name__ == '__main__':
    n = int(input("Введите натуральное число: "))
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
