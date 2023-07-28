code= ["red","green"]
def correctData(playerCombo):
    if len(playerCombo) != 2:
        return False
    for color in playerCombo:
        if color.lower() not in code:
            return False
    return True

response = input("Enter your color's combo, please ! Colors must be separate by commas format and no space are allowed(red,yellow) ")
print(correctData(response.split(",")))