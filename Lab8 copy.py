'''
Author: Sophie Johnson
Date: November 28
Purpose: To do a webscrape for netpass usernames and passwords
'''
import urllib.request

def scrape(url,names,netpass):
    '''
    This function identifies names and corresponding netpass IDs and adds them to
    lists
    Args: a url,an empty list to add names to, and empty list to add netpassIDs to
    Returns: none
    '''
    data=urllib.request.urlopen(url)
    theNames= data.readlines()

    for x in range (len(theNames)):
        content= theNames[x].decode("utf-8")

        startUsername= content.find('portfolios.ithaca.edu/')
        endUsername= content.find('/">')
        startName= content.find('/">')
        endName= content.find("</a><br /><small>Class of 2018</small></li>")
        theFilter=content.find("</li>")
        theFilter2=content.find("directories")

        theName=""
        if(theFilter==-1):
            if(theFilter2==-1):
                if(startName>-1):
                    theName= content[startName+3:endName-10]
                names.append(theName)

                theUsername=""
                if(startUsername>-1):
                    theUsername= content[startUsername+22 : endUsername]
                netpass.append(theUsername)

        
            

        

    #for all of the data read from the webpage
    #  identify where the names and netpass IDs appear
    #  identify the beginning and end points of where the data is contained
    #  slice out the appropriate parts and add to the lists

def printLogins(name,net):
    '''
    Print all of the name and netpass information
    Args: a list of names, a list of netpass IDs
    Return: none
    '''
    for x in range(len(name)):
        if(name[x]!=""):
            print(name[x], net[x])
        
                

    #Print each name followed by it's netpass

def main():
    '''
    Run the webscraping function and print results
    Args: none
    Return: none
    '''
    net=[]
    names=[]
    scrape("http://www.ithaca.edu/directories/eportfolios.php",names,net)
    
    
    printLogins(names,net)

main()
