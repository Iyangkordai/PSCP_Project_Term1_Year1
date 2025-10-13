"""test ch 4"""

def main():
    """Main"""
    n = int(input())
    customer_info = []
    room_list = [0] * 30
    for _ in range(n):
        name = input()
        idx1 = name.find(" ")
        idx2 = name.find(" ", idx1 + 1)
        check_in_day = name[idx1 + 1: idx2]
        check_out_day = name[idx2 + 1:]
        name = name[:idx1]
        customer_info.append([name, check_in_day, check_out_day])
        for i in range(int(check_in_day), int(check_out_day)):
            room_list[i] += 1
    for i in customer_info:
        print(f"{i[0]} >> Check in: {i[1]}, Check out : {i[2]}")
    total_room = 0
    for i in room_list:
        if total_room < i:
            total_room = i
    print(f"Total Room : {total_room}")

main()
sd