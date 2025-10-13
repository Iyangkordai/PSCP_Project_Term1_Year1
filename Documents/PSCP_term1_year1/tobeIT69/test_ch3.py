"""Test Ch3"""

def main():
    """Main"""
    text = input()
    astra = 0
    veyra = 0
    drak = 0
    for i in text:
        if i.isalpha():
            if i.lower() in ("a", "e", "o", "i", "u"):
                astra += 1
            if i.islower():
                veyra += 1
        else:
            drak += 1
    ae = astra * 5 + veyra * 3 - drak
    if 10 <= ae <= 20:
        spell = "Blades of starlight pierce through the void!"
        action = "ASTRAL RIFT SABER"
    elif 21 <= ae <= 35:
        spell = "Flames of rebirth, ignite and consume my destiny!"
        action = "PHOENIX ASCENSION"
    elif 36 <= ae <= 45:
        spell = "O frozen crown of silence, entomb my enemies in eternal sleep!"
        action = "GLACIAL OBLIVION"
    elif ae >= 46:
        spell = "Awaken, forbidden scripture - rewrite fate itself!"
        action = "ARCANUM: CODE-X"
    else:
        spell = "Error Code 999: please try again next life"
        action = ""
    print(":: PROTOCOL INITIATED ::")
    print(f"<---{spell}--->")
    if action:
        print(f">>> [{action}] <<<")
    print(":: PROTOCOL END ::")

main()
