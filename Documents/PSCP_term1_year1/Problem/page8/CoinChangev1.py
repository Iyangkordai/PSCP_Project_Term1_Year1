"""CoinChange V1"""

def main():
    """main"""
    change_money = int(input())
    cnt = 0
    cnt += change_money // 25
    change_money -= 25 * (change_money // 25)
    cnt += change_money // 10
    change_money -= 10 * (change_money // 10)
    cnt += change_money // 5
    change_money -= 5 * (change_money // 5)
    cnt += change_money
    print(cnt)

main()
