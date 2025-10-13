"""Stair"""

def main():
    """Main"""
    weight_step = int(input())
    n = int(input())
    ans = 0
    height = []
    for _ in range(n):
        height.append(int(input()))
    step = weight_step
    for i in height:
        if i > weight_step:
            ans = 0
            break
        if i <= step and step == weight_step:
            ans += 1
            step -= i
        elif i <= step and step != weight_step:
            step -= i
        elif i > step:
            step = weight_step
            step -= i
            ans += 1
    if not ans:
        print("NO")
    else:
        print(ans)

main()
