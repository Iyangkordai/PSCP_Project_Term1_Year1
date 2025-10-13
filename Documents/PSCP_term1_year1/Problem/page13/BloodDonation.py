"""Blood Donation"""

def main():
    """Main"""
    age = int(input())
    weight = int(input())
    donate_cnt = int(input())
    agree = ""
    if age == 17 or 60 <= age <= 70:
        agree = input()
    if age < 17 or age > 70:
        print("No")
    else:
        if weight >= 45:
            if not donate_cnt:
                if 17 < age <= 55 or (age == 17 and agree == "True"):
                    print("Yes")
                else:
                    print("No")
            else:
                if (17 < age <= 59) or ((age == 17 or (60 <= age <= 70)) and agree == "True"):
                    print("Yes")
                else:
                    print("No")
        else:
            print("No")

main()
