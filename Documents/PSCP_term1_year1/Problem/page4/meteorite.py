"""Meteorite"""

def main():
    """Main"""
    a = float(input())
    b = int(input())
    c = float(input())
    if a < c:
        print(0)
    else:
        cnt = 0
        ans = 1
        weight_per = a / b
        while weight_per >= c:
            weight_per /= b
            cnt += 1
            ans += b ** cnt
        print(f"{ans:.0f}")

main()
