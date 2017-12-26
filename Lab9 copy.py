'''
Author: Sophie Johnson
Date: December 5, 2017
Purpose: To match users with a dog
'''

def smallOrLargeDog(userInput, dogs):
    '''
    Purpose: to find a small or large dog
    Args: userInput
    Return: List of small or large dogs
    '''
    if (userInput== "small" or userInput=="Small"):
        newList=dogs[0:4]
    if (userInput=="large" or userInput=="Large"):
        newList= dogs[4:8]

    return(newList)

def calmOrEnergetic(userInput, theSizeList):
    '''
    Purpose: to find a calm or energetic dog that is small or large
    Args: userInput theSizeList
    Return: two remaining dog choices
    '''
    if (userInput== "calm" or userInput=="Calm"):
        newerList=theSizeList[2:4]

    if (userInput== "energetic" or userInput=="energetic"):
        newerList= theSizeList[0:2]

    return(newerList)

def hypoOrNah(userInput, thePersonalityList):
    '''
    Purpose: to find the final doggo
    Args: userInput thePersonalityList
    Return: the dog
    '''
    if (userInput== "yes" or userInput=="yes"):
        theDog= thePersonalityList[0]

    if (userInput== "no" or userInput=="no"):
        theDog= thePersonalityList[1]

    return(theDog)
    
def main():

    dogs=["Izzy","Lizzie", "Sam", "Oakie", "Chloe", "Ralph", "Rudy", "Leo"]

    
    print("Hi! Welcome to the dog matching program. We will ask you a series of questions to pair you with a dog.")

    smallOrLarge= input("Do you want your dog to be small or large? ")
       
    theSizeList=smallOrLargeDog(smallOrLarge, dogs)
    

    calmOrEnergeticDog= input("Do you want your dog to be calm or energetic? ")
       
    thePersonalityList= calmOrEnergetic(calmOrEnergeticDog, theSizeList)

        
    yesOrNoHypoAllergenic= input("Does your dog need to be hypoallergenic? ")
    theDoggo= hypoOrNah(yesOrNoHypoAllergenic, thePersonalityList)
        

    print("Your dog is", theDoggo, "!")
        

main()
