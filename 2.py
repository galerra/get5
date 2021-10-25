# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

import math

if __name__ == "__main__":
    x = int(input("x: "))
    y = 0
    if x <= 3.5:
        y = 2 * x * x + math.cos(x)
    elif x <= 5:
        y = x + 1
    else:
        y = math.sin(2 * x) - x * x
    print("y =", y)
