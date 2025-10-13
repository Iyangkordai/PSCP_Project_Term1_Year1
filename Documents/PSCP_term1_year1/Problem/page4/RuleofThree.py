"""RuleOfThree"""

def main():
    """Main"""
    q = int(input())
    price_ans = 0
    net_ans = 0
    for i in range(q):
        price = float(input())
        net = float(input())
        if not i:
            price_ans = price
            net_ans = net
            value_ans = net / price
        else:
            value_now = net / price
            if value_now > value_ans:
                net_ans = net
                price_ans = price
                value_ans = value_now
            elif value_now == value_ans:
                if price_ans > price:
                    price_ans = price
                    net_ans = net
    print(f"{price_ans:.2f} {net_ans:.2f}")

main()
