#Cleaning service
# This program would allow user to choose what type of cleaning service they
# want and how many room they want serviced to give a final estimate


#def Welcome():
    





def prompt_cus():
    #prompt user for cleaning service type
    cService = eval(input('What type of cleaning service do you want? \n  1-Floor Cleaning \n  2-Bathroom \n'))

    #validate cService input
    if(cService <= 0 or cService > 2):
        print("Please choose a service number that's avalible?")
        cService = eval(input('What type of cleaning service do you want? \n  1-Floor Cleaning \n  2-Bathroom \n'))


 
   #prompt for number of rooms needing sercice
    numRooms = eval(input('how many rooms are you needing service here? \t'))

    #validate number of rooms input
    if(numRooms <= 0):
        print('Please enter a valid room number count')
        numRooms = eval(input('how many rooms are you needing serviced here? \t'))
    
    #prompt for speed service or 2 day wait
    urgency = input('Would you like to order a speedy service or two day wait? \n  "+" for speed service \n "-" for two day wait')

    return(cService,numRooms,urgency)
def caculate_customerCost(cService,numRooms,urgency):
    #set price for service based on number of rooms with floor service 
    if(cService == 1):

        if(numRooms > 0 and numRooms <= 2):       
            serviceCost = 25                             #room less than 2 service cost 25$ each for loor leaning
        
        elif(numRooms <= 4):
            serviceCost = 35                             #rooms 2-4 service cost 35$ each for floor cleaning

        else:
            serviceCost = 45                             #room more than 4 service cost 45$ each floor cleaning



    #set price for service based on number of rooms with bathroom service 
    elif(cService == 2):
        if(numRooms > 0 and numRooms <= 2):
            serviceCost = 60                             #room less then 2 service cost is 60$ for bathroom cleaning

        elif(numRooms <= 4):
            serviceCost = 80                             #room 2-4 service cost is 80$ for bathroom cleaning

        else:
            serviceCost = 105                            #room higher than 4 service cost 105$ 

    #calculate total price based off urgency or normal wait
    if(urgency == '-'):
    
        totalCost = numRooms * serviceCost

    elif(urgency == '+'):
        totalCost = numRooms * serviceCost + 50


    return(totalCost)

def print_total(totalCost):
    #print service total cost
    print('Your total cost: ',totalCost)
    
    
    
















def main():
    #welcome()
    cService,numRooms,urgency = prompt_cus()
    totalCost = caculate_customerCost(cService,numRooms,urgency)
    print_total(totalCost)
    
main()
    
