"""Cyan's password generator"""

def main():
    """Main"""
    name = input()
    surname = input()
    age = input()
    if len(name) >= 5 and len(surname) >= 5:
        print(f"{name[:2]}{surname[len(surname) - 1]}{age[len(age) - 1]}")
    else:
        print(f"{name[0]}{age}{surname[len(surname) - 1]}")

main()
