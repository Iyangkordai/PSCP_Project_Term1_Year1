"""Season"""

def main():
    """Main"""
    month = int(input())
    date = int(input())
    ans = ""
    if month in (1, 2, 3):
        ans = "winter"
    elif month in (4, 5, 6):
        ans = "spring"
    elif month in (7, 8 , 9):
        ans = "summer"
    elif month in (10, 11, 12):
        ans = "fall"
    if date >= 21:
        match month:
            case 3:
                ans = "spring"
            case 6:
                ans = "summer"
            case 9:
                ans = "fall"
            case 12:
                ans = "winter"
    print(ans)

main()
