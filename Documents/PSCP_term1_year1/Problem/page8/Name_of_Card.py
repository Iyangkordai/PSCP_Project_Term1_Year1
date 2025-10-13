"""Name of Card"""

def main():
    """Main"""
    text = input().upper()
    number = text[:len(text) - 1]
    type_card = text[len(text) - 1:]
    name_of_card = ""
    match number:
        case "Q":
            name_of_card += "Queen"
        case "K":
            name_of_card += "King"
        case "J":
            name_of_card += "Jack"
        case "A":
            name_of_card += "Ace"
        case _:
            name_of_card += number
    name_of_card += " of "
    match type_card:
        case "D":
            name_of_card += "Diamonds"
        case "H":
            name_of_card += "Hearts"
        case "S":
            name_of_card += "Spades"
        case "C":
            name_of_card += "Clubs"
    print(name_of_card)

main()
