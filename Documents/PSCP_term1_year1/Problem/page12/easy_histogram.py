"""Easy Histogram"""

def main():
    """Main"""
    text = input()
    text_list = []
    for i in text:
        if i.isalpha():
            text_list.append(i)
    check_set = list(set(text_list))
    check_set.sort(reverse=True)
    check_set.sort(key=lambda x: x.lower())
    for i in check_set:
        cnt = 0
        for j in text_list:
            if j == i:
                cnt += 1
        print(f"{i} = {cnt}")

main()
