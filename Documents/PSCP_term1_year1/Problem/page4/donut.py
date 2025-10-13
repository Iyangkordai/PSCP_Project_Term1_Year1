"""Donut"""

import math as m

def main():
    """Main"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    set_donut = 0
    piece = 0
    if c and b:
        set_donut = m.floor(d / (b + c))
    if (set_donut + 1) * b  * a <= ((d - (set_donut * (b + c))) + set_donut * b ) * a:
        set_donut += 1
    if set_donut * (b + c) < d:
        piece = d - (set_donut * (b + c))
    all_donut = set_donut * (b + c) + piece
    price_t = (set_donut * b + piece) * a
    print(int(price_t), int(all_donut))
main()
