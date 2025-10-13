"""Key"""

def main():
    """Main"""
    id_str = input()
    sum_id = 0
    for i in id_str:
        sum_id += int(i)
    sum_id += (int(id_str[10:]) * 10)
    sum_id = str(sum_id)
    if len(sum_id) > 4:
        print(sum_id[(len(sum_id) - 4):])
    elif int(sum_id) < 1000:
        print(int(sum_id) + 1000)
    else:
        print(sum_id)

main()
