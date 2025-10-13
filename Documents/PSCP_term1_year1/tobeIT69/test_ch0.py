"""Hang Man"""

def main():
    """Main"""
    pitch = input().lower()
    cnt = 0
    err_cnt = 0
    check = ""
    state = 1
    while cnt < 5:
        si = input().lower()
        if len(si) != len(pitch):
            err_cnt += 1
            if err_cnt == 3:
                break
            print("Please try again!!!")
            continue
        else:
            err_cnt = 0
            for i in range(len(pitch)):
                if pitch[i] == si[i]:
                    check += "O"
                else:
                    check += "X"
            print(check)
            check = ""
        if si == pitch:
            print("Si WIN")
            state = 0
            break
        else:
            cnt += 1
    if state:
        print("Pitch WIN")

main()
