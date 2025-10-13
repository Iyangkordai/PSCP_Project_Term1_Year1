"""ProgressiveTax"""

import math as m

def main():
    """Main"""
    money = int(input())
    tax = 0
    if money > 4000000:
        tax += (money - 4000000) * 0.35
        money = 4000000
    if 2000000 < money <= 4000000:
        tax += (money - 2000000) * 0.3
        money = 2000000
    if 1000000 < money <= 2000000:
        tax += (money - 1000000) * 0.25
        money = 1000000
    if 750000 < money <= 1000000:
        tax += (money - 750000) * 0.2
        money = 750000
    if 500000 < money <= 750000:
        tax += (money - 500000) * 0.15
        money = 500000
    if 300000 < money <= 500000:
        tax += (money - 300000) * 0.1
        money = 300000
    if 150000 < money <= 300000:
        tax += (money - 150000) * 0.05
        money = 150000
    print(m.floor(tax))

main()
