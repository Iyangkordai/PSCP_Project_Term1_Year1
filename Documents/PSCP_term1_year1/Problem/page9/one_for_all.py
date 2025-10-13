"""One For All"""

def main():
    """Main"""
    n = int(input())
    ans = ""
    for i in range(1, n + 1):
        name = input()
        if i == n:
            ans += f"{name}_{i}"
        elif not i % 2:
            ans += name + "-" * i
        else:
            ans += name + "*" * i
    print(ans)

main()
