"""Align"""

import math as m

def main():
    """Main"""
    max_pai = int(input())
    align = input()
    text = input()
    match align:
        case "right":
            text = " " * (max_pai - len(text)) + text
        case "center":
            text = " " * (m.ceil((max_pai - len(text)) / 2)) \
            + text + " " * (max_pai - m.ceil((max_pai - len(text)) / 2))
    print(text)
main()
