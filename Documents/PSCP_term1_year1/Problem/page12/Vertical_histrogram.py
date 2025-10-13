"""Vertical Histogram"""

def main():
    """Main"""
    text = input()
    text_list = []
    for i in text:
        if i.isalpha():
            text_list.append(i)
    check_set = list(set(text_list))
    check_set.sort(key=lambda x: x.lower())
    check_set.sort(key=lambda x: x.isupper(), reverse=True)
    cnt_list = []
    for i in check_set:
        cnt_list.append(text_list.count(i))
    y = max(cnt_list)
    x = len(check_set)
    cnt2 = 0
    for i in range(y + 1):
        num_y = y - i
        cnt2 += cnt_list.count(num_y)
        cnt = cnt2
        for j in range(x + 1):
            white = " " * (2 - len(str(num_y)))
            if not j and i < y:
                print(f"{white}{y - i} ", end=" ")
            elif not j and i == y:
                print(" " * 3, end=" ")
            elif cnt_list[j - 1] >= num_y and i < y:
                cnt -= 1
                print("*", end=" " * (bool(cnt) and j < x))
                if not cnt:
                    break
            elif i == y:
                print(f"{check_set[j - 1]}", end=" " * (j < x))
            elif cnt:
                print(" ", end=" " * (j < x))
        print()

main()
