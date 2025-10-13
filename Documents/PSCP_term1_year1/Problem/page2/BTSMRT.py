"""BTSMRT"""

def main():
    """Main"""
    day = input()
    age = float(input())
    high = float(input())
    match day:
        case "Children Day":
            if age <= 14 and high <= 140:
                print("FREE")
            else:
                print("PAY")
        case "Senior Day":
            if age >= 60 or (age < 14 and high < 90):
                print("FREE")
            else:
                print("PAY")
        case "Normal Day":
            if age < 14 and high < 90:
                print("FREE")
            else:
                print("PAY")

main()
