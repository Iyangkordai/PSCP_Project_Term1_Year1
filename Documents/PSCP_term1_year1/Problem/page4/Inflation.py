"""Inflation"""

def main():
    """Main"""
    start_price = float(input())
    year = int(input())
    for _ in range(year):
        infla = start_price * 0.0381
        infla = int(infla * 1000)
    start_price *= 100
    start_price //= 1
    start_price /= 100
    print(start_price)

main()
