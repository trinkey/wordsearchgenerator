import random

def definevar(prompt, typeof, breaker = False):
    i = ""
    while not i:
        if typeof == "int":
            try: i = int(input(prompt))
            except ValueError: print("Bad input, try again."); i = ""
        elif typeof == "str": i = input(prompt)
        if breaker: break
    return i

width = definevar("Enter the width: ", "int")
height = definevar("Enter the height: ", "int")
words = definevar("Enter the words, seperated with \", \" (all spaces get removed in final word): ", "str").lower().split(", ")
lettersstr = definevar("Enter valid letters in one string, or leave blank for only a-z: ", "str", True)
letters = [char for char in ("abcdefghijklmnopqrstuvwxyz" if not lettersstr else lettersstr.lower())]

board = []
for i in range(height):
    board.append([""] * width)

checkamount = 1000
for i in words:
    i = i.replace(" ","")
    validchecks = checkamount
    amountofchar = len(i)
    good = 0
    while validchecks and not good:
        good = 1
        if not random.randint(0, 2):
            try: position = random.randint(0, height - amountofchar)
            except ValueError: position = 0
            position2 = random.randint(0, width - 1)
            for j in range(amountofchar):
                try:
                    if board[position + j][position2] and board[position + j][position2] != [char for char in i][j]: good = 0
                except IndexError: good = 0
            if good:
                for j in [char for char in i]:
                    board[position][position2] = j
                    position += 1
        elif random.randint(0, 1):
            position = random.randint(0, height - 1)
            try: position2 = random.randint(0, width - amountofchar)
            except ValueError: position2 = 0
            for j in range(amountofchar):
                try:
                    if board[position][position2 + j] and board[position][position2 + j] != [char for char in i][j]: good = 0
                except: good = 0
            if good:
                for j in [char for char in i]:
                    board[position][position2] = j
                    position2 += 1
        else:
            try: position = random.randint(0, height - amountofchar)
            except ValueError: position = 0
            try: position2 = random.randint(0, width - amountofchar)
            except ValueError: position2 = 0
            for j in range(amountofchar):
                try:
                    if board[position + j][position2 + j] and board[position + j][position2 + j] != [char for char in i][j]: good = 0
                except: good = 0
            if good:
                offset = 0
                for j in [char for char in i]:
                    board[position + offset][position2 + offset] = j
                    offset += 1
        validchecks -= 1
        if not validchecks and not good:
            print("Unable to place word \"" + i + "\" after " + str(checkamount) + " attempts.")

output = ""
for i in board:
    for o in i:
        if o == "": output += random.choice(letters)
        else: output += o
    output += "\n"

print(output)
input("Press enter to close.\n")
