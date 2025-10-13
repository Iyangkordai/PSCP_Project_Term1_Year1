"""MissingNumber"""

def main():
    """Main"""
    goal_num = int(input())
    check_set = set(x for x  in range(1, goal_num + 1))
    set_user = set()
    while True:
        num = int(input())
        if not num:
            break
        set_user.add(num)
    ans = list(check_set - set_user)
    ans.sort()
    for i in ans:
        print(i)

main()
