"""Chapter 1"""

def main():
    """Main"""
    n = int(input())
    for _ in range(n):
        name = input()
        grade = input()
        rule = input()
        score = -5
        my_list = [0, 0, 0, 0]
        for i in rule:
            match i:
                case "1":
                    my_list[0] = -5
                case "2":
                    my_list[1] = -2
                case "3":
                    my_list[2] = -10
                case "4":
                    my_list[3] = -7
        for i in my_list:
            score += i
        print(f"{name} {grade} : {score}")

main()
