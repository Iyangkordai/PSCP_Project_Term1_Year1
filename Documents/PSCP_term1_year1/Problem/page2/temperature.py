"""Temmperauture"""

def main():
    """Main"""
    temp = float(input())
    unit = input()
    w_unit = input()
    if unit != "C":
        match unit:
            case "K":
                temp -= 273.15
            case "F":
                temp = (temp - 32) / 1.8
            case "R":
                temp = temp / 1.8 - 273.15
    match w_unit:
        case "K":
            temp += 273.15
        case "F":
            temp = temp * 1.8 + 32
        case "R":
            temp = (temp + 273.15) * 1.8
    print(f"{temp:.2f}")

main()
