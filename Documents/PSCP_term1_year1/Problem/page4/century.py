"""Century"""
import math as m
def main():
    """Main"""
    n = int(input())
    for _ in range(n):
        t = input()
        u = t[:4]
        year = int(t[5:])
        match u:
            case "B.E.":
                year = m.ceil((year - 543) / 100)
            case "A.D.":
                year = m.ceil(year / 100)
            case _:
                year = -1
        if year > 0:
            print(year)
        else:
            print("ERROR")

main()
