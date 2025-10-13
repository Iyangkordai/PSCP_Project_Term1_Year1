"""Count Vowel"""

def main():
    """Main"""
    n = int(input())
    count = 0
    for _ in range(n):
        alpha = input().upper()
        if alpha in ("A", "E", "I", "O", "U"):
            count += 1
    print(count)

main()
