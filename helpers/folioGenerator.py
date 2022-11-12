import random


def folioG():
    numbersAndLetters = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k']    
    arr = []

    for i in numbersAndLetters:

        arr.append(random.choice(numbersAndLetters))

    strId = "".join(arr)

    return strId 


