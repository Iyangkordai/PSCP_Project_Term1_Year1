"""Christmas Light"""

def main():
    """Main"""
    light = input()
    match light:
        case "R":
            light_set = ["Red" , "Green" , "Blue"]
        case "G":
            light_set = ["Green" , "Blue", "Red"]
        case "B":
            light_set = ["Blue", "Red", "Green"]
    num = int(input())
    for i in range(num):
        print(light_set[i % 3], end=" ")

main()
