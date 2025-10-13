"""fiveX"""

def main():
    """Main"""
    num = int(input())
    for i in range(1, num + 1):
        if not i % 5:
            print("X", end=" " * (i == num))
        else:
            print("*", end=" " * (i == num))

main()
