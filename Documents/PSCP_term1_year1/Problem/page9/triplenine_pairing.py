"""999 Pairing"""

def main():
    """Main"""
    len_num = int(input())
    num1 = input()
    num2 = input()
    cnt = 0
    for i in range(len_num):
        if int(num1[i]) + int(num2[i]) == 9:
            cnt += 1
    if cnt == len_num:
        print("YES")
    else:
        print(f"NO {len_num - cnt}")

main()
