'''
Author: Sophie Johnson
Date: November 8, 2017
Purpose: To create the game hangman
'''
from random import *

def pickWord(theWordChoices):
    '''
    Purpose: To select a word for hangman 
    Args: wordList
    Return: selected word
    '''
    randomWord= randint(0,len(theWordChoices)-1) #this chooses a random index in the list
    theWord=theWordChoices[randomWord] #this assigns this random index to the word
    return theWord

def letterRight(letter, fullWord, wordList): 
    '''
    Purpose: To see if the letter is in the word
    Args: fullWord, userLetter, and wordList(this is the word with spaces that appears to the user)
    Return: False, or the newly formed word list 
    '''
    rightOrWrong=False #this variable will be the return. If the letter is in the word, it will be set to True.
    for y in range (len(fullWord)):
        if (fullWord[y]==letter):
            letterPlacement(wordList, y, letter)
            rightOrWrong=True
    return rightOrWrong
    

def letterPlacement(theWord, s, userLetter): #this function places the letter in the word that will be printed to users.
    '''
    Purpose: to write rewrite the word after a correct letter is found
    Args: theWord and s and userLetter
    Returns: new word list
    '''
    theWord[s]= userLetter 
    
    

def hangMan(theBodyList, theWrongGuess): #this function determines which body part will be hung
    '''
    Purpose: to hang body part if user guesses wrong
    Args: theBodyList and theWrongGuess
    Return: theBodyList(theWrongGuess)   
    '''
    return theBodyList[theWrongGuess]
    

 
    



def main():
    wordList= [ "kitten", "puppy", "book", "desk", "notebook", "lake", "ithaca", "edamame", "pretzel", "telephone", "foot"]
    bodyList= ["right arm", "left arm", "right leg", "left leg", "body" ,"head"]
    wrongGuess= 0 #This is a counting variable, allowing the program to stop when all the body parts have been hung.
    word=pickWord(wordList)

    running=True #This will later be set to false to stop loop once the user either wins or loses

    theWordList=[] #This will be where the correct user guesses are stored, along with the blank spaces represented by "_"

    for x in range (len(word)): #This is adding the blank spaces based upon the length of the word. This will be printed to users.  
        theWordList.append("_")
    
    for y in range(len(theWordList)): 
        print(theWordList[y], end="")
    print()



    while(running):


        userLetter= input("Guess a letter: ")
        userLetter= userLetter.lower()
        


        checkLetter=letterRight(userLetter, word, theWordList)

        if (checkLetter==False):
            bodyPart=hangMan(bodyList, wrongGuess)
            print("Draw body part: ", bodyPart)
            wrongGuess=wrongGuess+1
    
            for y in range(len(theWordList)): 
                print(theWordList[y], end="")
            print()

            if (wrongGuess==6):
                print("Game lost! Word is: ", word)
                running=False #This stops the program once the user guesses wrong 6 times.
 
      
        else:
            print("Correct guess!")
    
            for y in range(len(theWordList)): 
                print(theWordList[y], end="")
            print()
        
            if ("".join(theWordList) == word):
                print("You won! Word is: ", word)
                running=False #This stops the program once the user wins.
               
main()
