"""PhoneNumber"""

def main():
    """Main"""
    phone_num = input()
    state = input()
    if len(phone_num) == 9:
        phone_num = f"0 {phone_num[1:5]} {phone_num[5:]}"
    else:
        phone_num = f"{phone_num[:2]} {phone_num[2:6]} {phone_num[6:]}"
    if state == "International":
        phone_num = "+66" + phone_num[1:]
    print(phone_num)

main()
