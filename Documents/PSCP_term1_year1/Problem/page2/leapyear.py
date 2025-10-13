"""LeapYear"""

def main():
    """Main"""
    year = int(input())
    if (not year % 4 and year % 100) or not year % 400:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

main()
