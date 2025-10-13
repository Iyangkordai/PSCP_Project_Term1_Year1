"""SurprisingVote"""

import math as m

def main():
    """Main"""
    t_score = int(input())
    most = int(input())
    if most - m.floor((t_score - most) / 2) >= 2:
        print("Surprising")
    else:
        print("Not surprising")

main()
