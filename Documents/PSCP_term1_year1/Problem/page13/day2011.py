"""Day 2011"""

def main():
    """Main"""
    date = int(input())
    mounth = int(input())
    mounth_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    day = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    for i in range(mounth - 1):
        date += mounth_list[i]
    print(day[date % 7])

main()
