"""Hamming"""

def main():
    """Main"""
    text1 = input()
    text2 = input()
    lenge = min(len(text1), len(text2))
    cnt = 0
    for i in range(lenge):
        if text1[i] != text2[i]:
            cnt += 1
    print(cnt)

main()
