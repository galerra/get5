# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    x = int(input("x: "))
    y = int(input("y: "))
    R = int(input("R: "))

    r = (x ** 2 + y ** 2) ** 0.5

    if r > R:
        print("Не принадлежит")
    else:
        print("Принадлежит")
    