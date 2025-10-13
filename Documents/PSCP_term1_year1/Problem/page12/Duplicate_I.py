"""Duplicate I"""

def main():
    """Main"""
    m = int(input())
    n = int(input())
    groupA = set()
    groupB = set()
    for _ in range(m):
        groupA.add(int(input()))
    for _ in range(n):
        groupB.add(int(input()))
    ans = list(groupA & groupB)
    ans.sort(reverse=True)
    if not ans:
        print("Nope")
    else:
        print(*ans, sep="\n")

main()
