"""Heads and Legs"""

def main():
    """Main"""
    a = int(input())
    b = int(input())
    rabbit = b  / 2 - a
    bird = a - rabbit
    if 0 <= rabbit <= a and 0 <= bird <= a and rabbit.is_integer() and bird.is_integer():
        print(int(rabbit), int(bird))
    else:
        print("Impossible")

main()
