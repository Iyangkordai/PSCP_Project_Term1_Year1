"""Chapter 2"""

def main():
    """Main"""
    text = input().lower()
    ans = ""
    cnt_sra = 0
    for i in text:
        if i.isalpha():
            if i in ("a", "e", "i", "o", "u"):
                ans += i.upper()
                cnt_sra += 1
            else:
                ans += i
    print(ans)
    print((len(ans) * 5) + (cnt_sra * 10))

main()
