"""Quadrant"""

def main():
    """Main"""
    x = int(input())
    y = int(input())
    if not x and not y:
        print("O")
    elif not x and y:
        print("Y")
    elif x and not y:
        print("X")
    elif x > 0 and y > 0:
        print("Q1")
    elif y < 0 < x:
        print("Q4")
    elif x < 0 < y:
        print("Q2")
    else:
        print("Q3")

main()
