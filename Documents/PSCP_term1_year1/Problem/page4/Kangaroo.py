"""Kangaroo"""

def main():
    """Main"""
    a = int(input())
    b = int(input())
    c = int(input())
    cnt = 0
    d_ab = abs(a - b)
    d_bc = abs(b - c)
    while a != b != c:
        if d_ab >= d_bc:
            c = b
            b = d_ab // 2 + a
        else:
            a = b
            b = d_bc // 2 + b
        d_ab = abs(a - b)
        d_bc = abs(b - c)
        cnt += 1
    print(cnt)

main()
