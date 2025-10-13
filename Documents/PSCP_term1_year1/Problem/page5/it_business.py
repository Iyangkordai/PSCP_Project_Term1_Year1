"""IT Business"""

def main():
    """Main"""
    acc_money = float(input())
    cash = float(input())
    error_cnt = 0
    while True:
        if error_cnt >= 3:
            break
        action = input()
        if action.lower() == "end":
            break
        money = float(action[2:])
        action = action[:1]
        match action:
            case "D":
                if money <= cash:
                    cash -= money
                    acc_money += money
                    error_cnt = 0
                else:
                    error_cnt += 1
            case "W":
                if money <= acc_money:
                    cash += money
                    acc_money -= money
                    error_cnt = 0
                else:
                    error_cnt += 1
    print(f"{acc_money:.2f}")
    print(f"{cash:.2f}")

main()
