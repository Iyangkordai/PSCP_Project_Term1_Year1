studen_list = []
while True:
    text = input()
    if text == "END":
        break
    studen_list.append(int(text))

studen_list.sort()
print("-------------------")
for i in studen_list:
    print(i)