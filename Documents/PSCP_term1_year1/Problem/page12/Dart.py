"""Dart"""

import math as m

def main():
    """Main"""
    num = int(input())
    score = 0
    for _ in range(num):
        x, y = input().split()
        x, y = int(x), int(y)
        d = m.sqrt(m.pow(x, 2) + m.pow(y, 2))
        if 0 <= d <= 2:
            score += 5
        elif 2 < d <= 4:
            score += 4
        elif 4 < d <= 6:
            score += 3
        elif 6 < d <= 8:
            score += 2
        elif 8 < d <= 10:
            score += 1
    print(score)

main()
