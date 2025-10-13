"""Coke"""

def main():
    """Main"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    discout = 0
    if b and d:
        discout = (d - 1) // b * (a - c)
    total = (d * a) - discout
    print(total)

main()
