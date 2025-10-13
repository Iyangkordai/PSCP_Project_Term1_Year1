"""113"""

def main():
    """Main"""
    number = input()
    while True:
        idx = number.find("113")
        if idx == -1:
            break
        if idx + 3 < len(number):
            number = number[:idx] + number[idx + 3:]
        else:
            number = number[:idx]
    print(number)

main()
