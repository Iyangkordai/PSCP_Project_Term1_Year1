
"""US Interstate Number System"""

def main():
    """Main"""
    road_num = input()
    lenge = len(road_num)
    road_type = ""
    if road_num[-1] in ("0", "5"):
        if 1 <= lenge <= 2 :
            if road_num[-1] == "0":
                road_type = "Horizontal Major Interstate"
            elif road_num[-1] == "5":
                road_type = "Vertical Major Interstate"
            road_num = int(road_num)
        elif lenge == 3:
            if not int(road_num[0]) % 2:
                road_type = "Even Minor Interstate"
            else:
                road_type = "Odd Minor Interstate"
            road_num = int(road_num[1:])
    if road_type and (5 <= road_num <= 95):
        print(road_type)
        print(f"I-{road_num}")
    else:
        print("Others")
main()
