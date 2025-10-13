"""GCD_v2"""

def main():
    """Main"""
    num1 = int(input())
    num2 = int(input())
    ans = 0
    if num1 or num2:
        for i in range(1, min(num1 , num2) + 1):
            if not num1 % i and not num2 % i:
                if ans < i:
                    ans = i
    print(ans)

main()
