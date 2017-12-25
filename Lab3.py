"""
Author: Sophie Johnson
Purpose: To output drink and meal choice for users
Date: 9/26/17
"""

userFood= input("Do you want fish and vegetables, steak and baked potato, or burger and fries?")
userAge= int(input("What is your age?"))

if (userFood== "fish and vegetables" or userFood == "Fish and Vegetables"):
    if (userAge<21):
        print("Fish and vegetables with iced tea")
    elif (userAge>=21):
        userDrink= input("Do you want iced tea or white wine?")
        if (userDrink== "iced tea" or userDrink== "Iced Tea"):
            print("Fish and vegetables with iced tea")
        elif (userDrink== "White Wine" or userDrink== "white wine"):
            print("Fish and vegetables with white wine")
    
elif (userFood=="steak and baked potato" or userFood=="Steak and Baked Potato"):
    if (userAge<21):
        print("Steak and baked potato with lemonade")
    elif (userAge>=21):
        userDrink= input("Do you want lemonade or red wine?")
        if (userDrink== "lemonade" or userDrink== "Lemonade"):
            print("Fish and vegetables with lemonade")
        elif (userDrink== "Red Wine" or userDrink== "red wine"):
            print("Fish and vegetables with red wine")
elif (userFood== "burger and fries" or userFood== "Burger and Fries"):
    if (userAge<21):
        print("Burger and fries with cola")
    elif (userAge>=21):
        userDrink= input("Do you want cola or beer?")
        if (userDrink== "cola" or userDrink== "Cola"):
            print("Burger and fries with cola")
        elif (userDrink== "Beer" or userDrink== "beer"):
            print("Burger and fries with beer")
    
