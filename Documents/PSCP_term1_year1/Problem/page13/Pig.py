"""Pig"""

def main():
    """Main"""
    pair_n = int(input())
    pig = list(input().split())
    ans = []
    for i in range(pair_n):
        ans.append(max(int(pig[i * 2]), int(pig[i * 2 + 1])))
    if len(ans) > 1:
        for i,j in enumerate(ans):
            plus = " + " * (i < len(ans) - 1)
            print(f"{j}{plus}", end="")
        print(f" = {sum(ans)}")
    else:
        print(*ans)

main()
