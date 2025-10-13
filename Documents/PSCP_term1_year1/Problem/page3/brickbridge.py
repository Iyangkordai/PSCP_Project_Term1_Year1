"""BrickBridge"""

def main():
    """"Main"""
    a =  int(input())
    b = int(input())
    goal = int(input())
    goal -= 5 * min(b, goal // 5)
    if goal - a <= 0:
        print(goal)
    else:
        print("-1")

main()
