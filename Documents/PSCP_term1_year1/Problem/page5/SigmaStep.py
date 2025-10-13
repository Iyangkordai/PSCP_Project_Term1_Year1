"""SigmaStep"""

def main():
    """Main"""
    x = int(input())
    y = int(input())
    n = int(input())
    total = 0
    if not n and x and y:
        print("error")
    elif y <= 0 < x and n >= 0:
        print("error")
    elif x <= 0 and n <= 0 < y:
        print("error")
    elif x != y:
        for i in range(x , y + 1, n):
            total += i
        print(total)
    else:
        print(total)

main()
