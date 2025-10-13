"""Giraffe"""

def main():
    """Main"""
    num = int(input())
    cnt = 0
    height = []
    for _ in range(num):
        height.append(int(input()))
    lenge = len(height)
    for i,j in enumerate(height):
        if not i or i + 1 == lenge:
            if i + 1 < lenge and j > height[i + 1]:
                cnt += 1
            elif i - 1 >= 0 and j > height[i - 1]:
                cnt += 1
        else:
            if j > height[i + 1] and j > height[i - 1]:
                cnt += 1
    if lenge == 1:
        print(1)
    else:
        print(cnt)

main()
