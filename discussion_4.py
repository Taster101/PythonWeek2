
#This program caculates a runner total miles ran by taking his input of m iles ran today and miles ran in the past 



#create function to caculate miles

def compute_miles(num1,num2):

    total = num1 + num2                    #caculate total

    return total

#create function to prompt user
def prompt_user():
    miles_ran = eval(input('How many miles did you run today?   \n'))      #prompt user for miles ran
    miles_total = eval(input('how many miles did you run in the past?  \n'))  #prompt user for previous miles ran
    return(miles_ran,miles_total)


#create function to display miles
def print_miles(total):
    print('miles total:', total)                                      #print miles



#main function
def main():
    miles_ran,miles_total = prompt_user()
    total = compute_miles(miles_ran,miles_total)
    print_miles(total)

    

main()
    
