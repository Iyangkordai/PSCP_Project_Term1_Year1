"""Horizontal Histogram"""

def main():
    """Main"""
    text = input()
    text_list = []
    for i in text:
        if i.isalpha():
            text_list.append(i)
    text_set = list(set(text_list))
    text_set.sort(key=lambda x: x.lower())
    text_set.sort(key=lambda x: x.isupper())
    cnt_list = []
    for i in text_set:
        cnt_list.append(text_list.count(i))
    for i,j in enumerate(text_set):
        print(f"{j} : ", end="")
        for k in range(cnt_list[i]):
            print("-", end="")
            if not k % 4 and cnt_list[i] != 5 and k:
                print("|",end="")
        print()

main()
