"""Sequence X"""

def main():
    """Main"""
    num = int(input())
    for i in range(1, num * 2):
        end = num * 2 - abs(num - i)
        for j in range(1, end):
            if j == num:
                print(f"{(num - abs(num - i)):>02}" ,end=" " * (j < end - 1))
            elif i == num:
                print(f"{(num - abs(num - j)):>02}" ,end=" " * (j < end - 1))
            elif j >= abs(num - i) + 1:
                print(f"{(num - abs(num - i) - abs(num - j)):>02}" ,end=" " * (j < end - 1))
            else:
                print("  ", end=" " * (j < end - 1))
        print()
main()
