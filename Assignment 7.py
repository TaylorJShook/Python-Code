#Taylor Shook
#COP 2500
#Date: 3/27/23
#Assignment: Assingment 7 Code Database

#airport code finder
#takes parameters and uses them to decide what code the airport should have.
def airport_code_finder(a, c, m):
    #splits the airport name into words
    #Code for Name
    if(m=="name"):
        #uses if statements to determine the number of words
        name_words=a.split()
        if (len(name_words)== 2):
          code=name_words[0][0] + name_words[1][0]
        elif(len(name_words)>2):
            code = name_words[0][0] + name_words[1][0] + name_words[2][0]
        else:
            code=name_words[0][0]
        #returns the code for name method
        return code.upper()

    #Code for City
    elif(m=="city"):
        code=c[:3].upper()
        #returns the code for city method
        return code
    
    
  
    
    
#main function takes in parameters, calls the airport code finder function and writes into output file.
def main():
    #opens files
    file_in = open("us-airports.csv", "r", encoding="utf-8")
    file_out = open("output.csv", "w", encoding="utf-8")

    #reads in values from input file, cleans the inputs
    inputValues = file_in.read()
    cleaned_input = inputValues.strip()
    lines = cleaned_input.split("\n")
    
    #for loop takes cleaned lines from the file, splits the values    
    for i in range(len(lines)):
        values = lines[i].split(",")
        #second for loop takes the split values and uses them to call function
        for j in range(len(values)-1):
            values[j]= str(values[j])
            #gets codes for city and name methods
            codeN=airport_code_finder(values[0],values[1],"name")
            codeC=airport_code_finder(values[0],values[1],"city")
            #writes airport, city, and code values into the output file
            FileOutput=(values[0] + "," + values[1] + "," + codeN+ ", "+ codeC+"\n")
            file_out.write(FileOutput)
            
            
    #closing files
    file_out.close()
    file_in.close()

    #prints that the program is complete 
    print("--------------------------------")
    print("Done")
            
                        

    
#call to main function
main()
