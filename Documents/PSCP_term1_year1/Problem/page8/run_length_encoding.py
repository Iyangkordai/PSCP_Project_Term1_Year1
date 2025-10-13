"""Run Length Encoding"""

def main():
    """Main"""
    text = input() + " "
    encode_alpha = text[0]
    cnt = 0
    ans = ""
    for i in text:
        if encode_alpha == i:
            cnt += 1
        else:
            ans += f"{cnt}{encode_alpha}"
            cnt = 1
            encode_alpha = i
    print(ans)

main()
