"""CasearV1"""

def main():
    """Main"""
    num = int(input())
    text = input()
    decode_text = ""
    ascii_n = 0
    for i in text:
        if i.isalpha():
            if i.isupper():
                start_idx = ord("A")
                ascii_n = (ord(i) - start_idx + num)  % 26 + start_idx
            else:
                start_idx = ord("a")
                ascii_n = (ord(i) - start_idx + num) % 26 + 97
            decode_text += chr(ascii_n)
        else:
            decode_text += i
    print(decode_text)

main()
