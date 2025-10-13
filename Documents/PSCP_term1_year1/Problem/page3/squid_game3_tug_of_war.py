"""Squid game 3 - tug - of - war"""

def main():
    """Main"""
    team_A = 0
    tema_B = 0
    for _ in range(10):
        team_A += int(input())
    for _ in range(10):
        tema_B += int(input())
    if team_A > tema_B:
        print("B")
    elif tema_B > team_A:
        print("A")
    else:
        print("AB")

main()
