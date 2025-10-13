"""Ball"""

def main():
    """Main"""
    start_h = float(input())
    now_h = start_h * 3 / 5
    cnt = 0
    while now_h > 0.01:
        now_h *= 3 / 5
        cnt += 1
    print(cnt)

main()
