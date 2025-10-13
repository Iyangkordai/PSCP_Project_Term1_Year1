"""PongYa"""

def main():
    """Main"""
    num = input()
    if not int(num) % 3 or num[len(num) - 1] == "3":
        print("PONG")
    else:
        print(num)

main()
