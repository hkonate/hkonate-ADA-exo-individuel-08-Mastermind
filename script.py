from random import randint

options=["yellow", "red", "blue", "green", "orange", "purple", "grey", "black"]
result = [0,0]
code = []
def randomColor():
    index = 0
    while index < 4:
        code.append(options[randint(0,7)])
        index += 1
    print(code)

def correctData(playerCombo):
    if len(playerCombo) != 4:
        return False
    index = 0
    while index < 4:
        if playerCombo[index].lower() in code:   
            if playerCombo[index].lower() == code[index]:
                result[0] += 1
            else:
                result[1] += 1
        else:
            return False
        index += 1
    if result[0] == 4:
        return True
    else:
        return False

def gamePlay(count):
    response = input("Enter your color's combo, please ! Colors must be separate by commas format and no space are allowed(color,color) ")
    itIsTheEnd = correctData(response.split(","))
    if itIsTheEnd == False:
        count -= 1
        if count <= 0:
            print("You tried twelve times and did not find the secret code, sorry but you lost !\nThe secret code was {}".format(code))
            return False
        print("{}, attempt left is {}".format(result, count))
        result[0] = 0
        result[1] = 0
        gamePlay(count)
    else:
        print("Congratulation you found the secret combo !")

randomColor()
gamePlay(12)