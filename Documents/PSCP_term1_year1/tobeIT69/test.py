"""test"""

def main():
    """Main"""
    r_cnt = 0
    p_cnt = 0
    b_cnt = 0
    g_cnt = 0
    o_cnt = 0
    while True:
        color_n = input()
        if color_n == "-1":
            break
        match color_n:
            case "R":
                r_cnt += 1
            case "B":
                b_cnt += 1
            case "P":
                p_cnt += 1
            case "G":
                g_cnt += 1
            case "O":
                o_cnt += 1
    cnt = int(input())
    print(f"R: {r_cnt * cnt} G: {g_cnt * cnt} B: {b_cnt * cnt} O: {o_cnt * cnt} P: {p_cnt * cnt}")

main()
