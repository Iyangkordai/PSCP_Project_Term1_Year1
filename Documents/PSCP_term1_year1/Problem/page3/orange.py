"""Orange"""

def main():
    """Main"""
    l = int(input())
    sell_n = int(input())
    total_orange = 0
    cnt = 0
    for i in range(1, l + 1):
        total_orange += i ** 2
    total_orange -= sell_n
    for i in range(l, 0, -1):
        total_orange -= i ** 2
        if total_orange < 0 and abs(total_orange) < l ** 2:
            cnt += 1
            break
        if total_orange > 0:
            cnt += 1
    print(cnt)

main()
