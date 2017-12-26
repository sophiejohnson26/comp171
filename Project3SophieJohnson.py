'''
Author: Sophie Johnson
Date: December 5, 2017
Purpose: To make three image filters, hopeify, checkboard, and flip. 
'''
from readwritePPM import *

def hopeify(theImg, height, width):
    '''
    Purpose: This function hopeify's the image by dividing the brightness of pixels
    into four different categories, and changing each category to a color.
    Args: theImg
    Return: the hopeified image saved in a new list
    '''
    newImg=[] #this is creating an empty list for the new image, so alterations are not made on the original one. This is repeated on each of the filters.
    
    for h in range(height):
        row=[] #empty list for the rows
        for w in range(width):
            newPixel=[] #empty list for each pixel
            avg= (theImg[h][w][0] + theImg[h][w][1] + theImg[h][w][2])/3

            if(avg>=200): #changes these brightnesses to red
                newPixel.append(255) #this proccess appends each color (red, green blue) to the newPixel list
                newPixel.append(0) 
                newPixel.append(0)

            if(avg<200 and avg>=120): #changes these brightnesses to blue
                newPixel.append(0)
                newPixel.append(0)
                newPixel.append(255)

            if(avg<120 and avg>=60): #changes these brightnesses to black
                newPixel.append(255)
                newPixel.append(255)
                newPixel.append(255)

            if(avg<60 and avg>=0): #changes these brightnesses to white
                newPixel.append(0)
                newPixel.append(0)
                newPixel.append(0)

            row.append(newPixel) #this appends the color created in newPixel to the list row

        newImg.append(row) #this appends all of the rows to the new image
  
    return(newImg)
                
        
def horizontalFlip(theImg):
    '''
    Purpose: This function will horizontally flip the image
    Args: theImg
    Return: the flipped image saved in a new list
    '''
    newImg=[]


    for x in range(len(theImg)):
        row=[]
        for y in range(len(theImg[0])):
            newPixel=[]
            for z in range(len(theImg[x][y])):
                newPixel.append(theImg[x][len(theImg[x])-y-1][z]) #this equation in the second index gets the second index to the index on the opposite side of the original image. 
            row.append(newPixel)

        newImg.append(row)

    return(newImg)


def checkerboard(theImg, height, width):
    '''
    Purpose: This function with checkerboard the image
    Args: theImg
    Return: the checkered image saved in a new list
    '''
    newImg=[]

    for h in range(height):
        row=[]
        for w in range(width):
            newPixel=[]
            for x in range(3):
                newPixel.append(theImg[h][w][x])
            
            for z in range (1,11):
                if (h>2*z*height/20 and w<2*z*width/20): #this is getting the location to put each dark checker mark
                    makeInverse(newPixel)
                if (h<2*z*height/20 and w>2*z*width/20): #this is getting the location to put each dark checker mark
                    makeInverse(newPixel)
   
            row.append(newPixel)

        newImg.append(row)

    return(newImg)
    
def makeInverse(pixel):
    '''
    Purpose: this function is making the inverse of each pixel for the checkerboard function.
    Args: pixel
    Return: none
    '''
    pixel[0]= 255-pixel[0]
    pixel[1] = 255-pixel[1]
    pixel[2] = 255-pixel[2]
   


def saveImage(theImg):
    '''
    Purpose: This function saves the image
    Args: theImg
    Return: None
    '''
    newName=input("What name do you want to save your image as? ")
    writePPM(newName+".ppm", theImg)

def main():
    running=True #this variable determines when the program is running
    imgName= input("Enter an image name: ")

    img=readPPM(imgName+".ppm") 

    
    
    width=len(img[0])
    height=len(img)


    while(running):

        userChoice= input("Do you want to hopeify your image, flip your image, checkerboard your image, save your image, or quit? ")


        if(userChoice== "hopeify" or userChoice=="hopeify"):
            theNewImg=hopeify(img, height, width)
            print("Your image has been hopeified! Select save image after the next prompt to save it and view it.")

        if(userChoice=="flip" or userChoice=="Flip"): 
            theNewImg=horizontalFlip(img)
            print("Your image has been flipped! Select save image after the next prompt to save it and view it.")
 
            

        if(userChoice=="checkerboard" or userChoice=="Checkerboard"):

            theNewImg=checkerboard(img, height, width)
            print("Your image has been checkered! Select save image after the next prompt to save it and view it.")

            

        if (userChoice== "save" or userChoice=="Save"): #users can decide when to save their images
            saveImage(theNewImg)
            print("Your image has been saved!")
            

        if (userChoice=="quit" or userChoice=="Quit"):
            running=False #this will stop the program

        
main()
