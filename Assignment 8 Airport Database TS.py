#Taylor Shook
#COP 2500
#Date:4/3/2023
#Assignment: Assignment 8


#Menu Function takes in user selection, returns it
def menu():
    selection=int(input("What would you like to do?\n1. Add airport\n2. Remove airport\n3. Access\n4. List airports\n5. Exit\n"))
    return selection

#Main function
def main():
    #creates dictionary named airports
    airports = {}
    #defines the variable choice as an int
    choice=0
    
    print("Welcome to OIA!")
    #while loop that runs until user chooses to exit
    while(choice!=5):
        #calls menu function, assigns the selection value to choice
        choice=menu()
        
        #if else statements
        #if 1. add airport
        if(choice==1):
            code= str(input("What is the airport's code?\n"))
            name=str(input("What is the airport's name?\n"))
            distance=int(input("What is the distance from Orlando?\n"))
            airports[code]= [name, distance]
            print("Added")
            
        #if 2. remove airport
        elif(choice==2):
            removeCode=str(input("What airport would you like to remove?\n"))
            #checks to see if value is in the dictionary
            if removeCode in airports.keys():
                #removes selected values
                del airports[removeCode]
                print("Removed")
            else:
                print("Airport does not exist")
                
        #if 3. access airport
        elif(choice==3):
            codeName=str(input("What is the code you would like to access?\n"))
            #checks if value is in dictionary
            if codeName in airports.keys():
                #prints selected values
                print(airports[codeName][0],"-",airports[codeName][1])
            else:
                print("Airport does not exist")
                
        #if 4. list airports
        elif(choice==4):
            #if statement checks if airports is empty
            if (airports):
                for key in airports.keys():
                    #prints name and distance of each code in for loop
                    print(airports[key][0],"-",airports[key][1])
            else:
                print("No Airports")
                
    #only displays once out of the while loop 
    print("Goodbye")

#calls the main function
main()
            
        
                
        

