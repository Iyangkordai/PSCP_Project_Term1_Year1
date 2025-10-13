"""Largest Number"""

def main():
    """Main"""
    num1 = input()
    num2 = input()
    num3 = input()
    set1 = int(num1 + num2 + num3)
    set2 = int(num1 + num3 + num2)
    set3 = int(num2 + num1 + num3)
    set4 = int(num2 + num3 + num1)
    set5 = int(num3 + num1 + num2)
    set6 = int(num3 + num2 + num1)
    ans = int(set1)
    if set2 > ans:
        ans = set2
    if set3 > ans:
        ans = set3
    if set4 > ans:
        ans = set4
    if set5 > ans:
        ans = set5
    if set6 > ans:
        ans = set6
    print(ans)

main()
