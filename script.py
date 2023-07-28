code= ["red","green","green","red"]
def correctData(playerCombo):
    if len(playerCombo) != 4:
        return False
    index = 0
    while index < len(code):
        if playerCombo[index].lower() != code[index]:
            return False
        index += 1
    return True

def gamePlay():
    response = input("Enter your color's combo, please ! Colors must be separate by commas format and no space are allowed(color,color) ")
    itIsTheEnd = correctData(response.split(","))
    if itIsTheEnd == False:
        gamePlay()
    else:
        print("Congratulation you found the secret combo !")

gamePlay()