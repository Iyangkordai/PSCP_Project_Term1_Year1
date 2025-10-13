"""Milik"""

def main():
    """Main"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    smt = 0
    smt2 = 0
    smt3 = 0
    if d:
        smt = d // a
    if b and smt and c:
        smt2 = (smt // b) * c
        smt3 = (smt2 // b) * c
    print(smt + smt2 + smt3)

main()
