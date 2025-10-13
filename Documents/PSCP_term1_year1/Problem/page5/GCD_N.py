"""GCD_N"""

import math as m

def main():
    """Main"""
    arr_num = []
    n = int(input())
    for _ in range(n):
        arr_num.append(int(input()))
    all_gcd = arr_num[0]
    for i in range(1, n):
        all_gcd = m.gcd(all_gcd, arr_num[i])
    print(all_gcd)

main()
