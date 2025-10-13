"""Tuple's Sad Life"""

def main():
    """Main"""
    my_lovely_tuple = tuple(input().split())
    want = input()
    cnt = my_lovely_tuple.count(want)
    word = my_lovely_tuple.index(want)
    word = (str(word) + " ") * cnt
    for _ in range(cnt):
        print(word[:len(word) - 1])

main()
