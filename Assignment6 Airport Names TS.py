#Taylor Shook
#COP 2500
#Date: 3/20/23
#Assignment: Assingment 6 Airport Names

#airport code finder
#takes parameters and uses them to decide what code the airport should have.
def airport_code_finder(a, c, m):
    #If statement determines whether the method is based on name or city
    if(m=="name"):
        #splits the airport name into words
        name_words=a.split()
        word1 = name_words[0]
        word2 = name_words[1]
        word3 = name_words[2]
        
        count=0
        code=""
        #for loop determines if there are 1 or 2 capital letters within the first word
        for i in range(len(word1)):
            if(word1[i].isupper()):
                code += word1[i]
                count += 1
                if(count==2):
                    code+=word1[i+1]
        if(count==1):
            code+=word2[0]
            code+=word3[0]
        #returns the code in all capitalized letters    
        return code.upper()
    
    elif(m=="city"):
        #returns the first 3 letters of the city, all capitalized
        return c[:3].upper()
    
  
    
    
#main function takes in parameters, calls the airport code finder function.
def main():
    airport=str(input("What is the name of the airport?\n"))
    city=str(input("What is the name of the city?\n"))
    method=str(input("What method should be used? Name or City?\n"))
    code=airport_code_finder(airport,city,method)
    print(airport,"-",city,"-",code)

    
#call to main function
main()
    
