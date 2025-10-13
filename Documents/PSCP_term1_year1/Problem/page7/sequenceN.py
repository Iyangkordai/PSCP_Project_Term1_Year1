"""Sequence N"""

def main():
    """Main"""
    num = int(input())
    for i in range(num):
        for j in range(num):
            if i == j or not j or j == num - 1:
                print("*", end="")
            else:
                print("",end=" " * (j < num - 1))
        print()

main()
