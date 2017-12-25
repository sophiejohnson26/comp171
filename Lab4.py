"""
Author: Sophie Johnson
Purpose: To do lab 4
Date: Oct 4, 2017
"""
running=True
loggedIn= False
userBalance=100

while (running):
    if(not loggedIn):
        print("You have to log in.")
        username=  input("Enter your username: ")
        password= input("Enter your password: ")
        while (username != "codingiscool22" or password != "ilikedogs55"):
            print("Incorrect username or password")
            username=  input("Enter your username: ")
            password= input("Enter your password: ")
    print("You have logged in.")
    loggedIn=True
    menu=True
    while(menu):
        action= input ("Do you want to withdraw, deposit, check balance, or log out?")
        if (action== "withdraw" or action== "Withdraw"):
            withdraw= int(input("How much do you want to withdraw?"))
            while (userBalance-withdraw<0):
                print("Insufficient funds", "Balance is:", userBalance)
                withdraw= int(input("How much do you want to withdraw?"))
            if (userBalance-withdraw>0):
                print("You have withdrawn: ", withdraw)
                print("New balance is: ", userBalance-withdraw)
        if (action== "deposit" or action== "Deposit"):
            deposit=int(input("How much do you want to deposit?"))
            userBalance= userBalance+deposit
            print("New balance is: ", userBalance)
        if (action== "check balance" or action=="Check Balance"):
            print("Balance is: ", userBalance)
        if (action=="log out" or action=="logout" or action=="Log Out"):
            print("You have logged out.")
            menu= False
            loggedIn=False


  

                
        
        
           



