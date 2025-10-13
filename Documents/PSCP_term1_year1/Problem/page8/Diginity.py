"""Diginity"""

def sum_of_number(n):
    """sum of number till len(n) == 1"""
    ans = 0
    while True:
        for i in n:
            ans += int(i)
        n = str(ans)
        if len(n) == 1:
            return ans
        ans = 0

def main():
    """Main"""
    while True:
        number = input()
        if number == "0":
            break
        print(sum_of_number(number))

main()
