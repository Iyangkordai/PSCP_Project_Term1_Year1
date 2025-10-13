"""Ramen Bowl"""

def main():
    """Main"""
    ramen_list = []
    for _ in range(int(input())):
        ramen_list.append(int(input()))
    ramen_set = list(set(ramen_list))
    ramen_list.sort()
    ramen_set.sort()
    ans = 0
    for i in ramen_set:
        cnt = ramen_list.count(i)
        ans = max(ans, cnt)
    print(ans)

main()
