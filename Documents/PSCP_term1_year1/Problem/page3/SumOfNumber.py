"""SumOfNumber"""

def main():
    """Main"""
    want_num = int(input())
    total = 0
    while True:
        n = int(input())
        if n == -1:
            break
        total += n
        if total == want_num:
            break
    print(total)

main()
