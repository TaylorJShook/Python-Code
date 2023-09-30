#Name: Taylor Shook
#Course Code: COP2500.0V04
#Date: 2/6/2023
#Assignment Title: Travel Times


print("Welcome to the travel planner\n")

#Asks user how many places they want to visit and how long they have in the day
numPlaces=int(input("How many places are we visiting today?\n"))
time=int(input("How much time (in minutes) do we have to visit today?\n"))

totalTime=0

#for loop that finds out how long it takes to travel and visit at each location
for count in range(1, numPlaces+1):
    print("How long does it take to travel to location #",(count),"?", sep="")
    travelTime=int(input("\n"))
    print("How long would you like to stay in location #",(count),"?", sep="")
    tripTime=int(input("\n"))
    #counter that keeps track of the total time spent traveling and visiting
    totalTime= totalTime + tripTime + travelTime


#Prints total time
print("This trip would take", totalTime,"minutes.")

#if statement decides whether or not there is enough time to complete the trip.
if(totalTime<=time):
    print("You are able to take this trip.")

else:
    print("You are not able to take this trip in time.")


