"""BigFrame"""

def main():
    """Main"""
    text1 = input().strip()
    text2 = input().strip()
    text3 = input().strip()
    text4 = input().strip()
    text5 = input().strip()
    lenge = max(len(text1), len(text2), len(text3), len(text4), len(text5))
    text1 += " " * (lenge - len(text1))
    text2 += " " * (lenge - len(text2))
    text3 += " " * (lenge - len(text3))
    text4 += " " * (lenge - len(text4))
    text5 += " " * (lenge - len(text5))
    print("*" * (lenge + 4))
    print(f"* {text1} *")
    print(f"* {text2} *")
    print(f"* {text3} *")
    print(f"* {text4} *")
    print(f"* {text5} *")
    print("*" * (lenge + 4))

main()
