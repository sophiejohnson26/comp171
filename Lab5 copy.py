'''
Purpose: to do lab 5
Date: Oct. 23, 2017
Author: Sophie Johnson
'''
def dayAge (userAge):
    '''
    Purpose: to determine age in days
    Arguments: User year age entered
    Return: age in days
    '''
    dayAge1=userAge*365
    return dayAge1

def hourAge (userAge):
    '''
    Purpose: to determine age in hours
    Arguments: User year age entered
    Return: age in hours
    '''
    hourAge1= userAge*8760
    return hourAge1

def minuteAge (userAge):
    '''
    Purpose: to determine age in minutes
    Arguments: User year age entered
    Return: Age in minutes
    '''
    minuteAge1= userAge*525600
    return minuteAge1

def secondAge (userAge):
    '''
    Purpose: to determine age in seconds
    Arguments: User year age entered
    Return: Age in seconds
    '''
    secondAge1= userAge*31536000
    return secondAge1

def main():
    yearAge= int(input("Enter your age in years: "))

    while(yearAge<=0):
        print("You cannot be zero years or younger!")
        yearAge= int(input("Enter your age in years: "))

    
    userDayAge=dayAge(yearAge)
    print ("Day Age: ", userDayAge)
    
    userHourAge= hourAge(yearAge)
    print("Hour Age:", userHourAge)

    userMinuteAge= minuteAge(yearAge)
    print("Minute Age:", userMinuteAge)

    userSecondAge= secondAge(yearAge)
    print("Second Age:", userSecondAge)
    

main()
