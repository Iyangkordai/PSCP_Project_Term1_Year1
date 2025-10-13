"""Saitama"""
import math as m
def main():
    """Main"""
    push_up = int(input())
    sit_up = int(input())
    look = int(input())
    run = int(input())
    push_up_limit = m.ceil(push_up / int(input()))
    sit_up_limit = m.ceil(sit_up / int(input()))
    run_limit = m.ceil(run / int(input()))
    look_limit = m.ceil(look / int(input()))
    ans = push_up_limit
    if sit_up_limit > ans:
        ans = sit_up_limit
    if look_limit > ans:
        ans = look_limit
    if run_limit > ans:
        ans = run_limit
    print(ans)

main()
