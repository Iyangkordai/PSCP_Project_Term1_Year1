"""Palinedrome"""

def main():
    """Main"""
    goal_cnt = int(input())
    start_t = input()
    idx = start_t.find(":")
    start_t = start_t[:idx] + start_t[idx + 1:]
    now_cnt = 0
    while True:
        if now_cnt == goal_cnt:
            break
        start_t = int(start_t)
        start_t += 1
        start_t %= 2400 
        if start_t == 2400:
            start_t = "0000"
        else:
            start_t = f"{start_t:>03}"
        if start_t == start_t[::-1]:
            now_cnt += 1
            start_t = int(start_t)
            print(f"{start_t // 100}:{start_t % 100:>02}")

main()
