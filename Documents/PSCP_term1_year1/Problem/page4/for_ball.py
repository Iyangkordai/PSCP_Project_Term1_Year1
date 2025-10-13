"""FOR!F-Ball"""

def main():
    """Main"""
    ball = 1
    text = input()
    for i in text:
        match i:
            case "A":
                if ball == 1:
                    ball = 2
                elif ball == 2:
                    ball = 1
            case "B":
                if ball == 2:
                    ball = 3
                elif ball == 3:
                    ball = 2
            case "C":
                if ball == 1:
                    ball = 3
                elif ball == 3:
                    ball = 1
    print(ball)

main()
