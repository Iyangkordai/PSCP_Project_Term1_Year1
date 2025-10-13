"""Divide 30 or 5"""

def main():
    """Main"""
    n = int(input())
    total = 0
    for i in range(1, n + 1):
        if not i % 3 or not i % 5:
            total += i
    print(total)

main()
