# Ptython
#This code will caculate a uber driver total earnings for the day




    

def main():
#prompt for miles driven
    numMiles = eval(input('how many miles did you drive?'))

#prompt for hours worked
    numHours = eval(input('how many hours did you work?'))

#prompt for tips earned
    totalTips = eval(input('how much did you earn in tips?'))

#intialize hourly rate
    hourlyRate = 15

#intialize commission rate
    comissionRate = .5

#calculate daily wage
    dailyWage = numHours * hourlyRate

#calculate commission earned
    comissionTotal = numMiles * comissionRate

#calculate total earned
    totalPay = dailyWage + comissionTotal + totalTips

#print daily wage 
    print('dailywage: \t',dailyWage)

#print comission
    print('total commission earned: \t',comissionTotal)

#print tips for the day
    print('total in tips:  \t',totalTips)

#print total paystatus
    print('total pay:  \t' ,totalPay)

main()



#Diccussion post 

def main():
#prompt for how many pizza's you want
    numPizza = eval(input("how many pizza do you want to order?"))

#prompt how many tacos you want
    numTaco = eval(input("how many taco's do you want to order?"))

#intialize taco price
    tacoPrice = 3.50

#intailize pizza price
    pizzaPrice = 5.00


#caculate toatal price for products
    totalPrice = (numPizza * pizzaPrice) + (numTaco * tacoPrice)

#print total price
    print('your tatal price is ' ,totalPrice)

main()

#Cleaning service
# This program would allow user to choose what type of cleaning service they
# want and how many room they want serviced to give a final estimate


def main():

  #prompt user for cleaning service type
    cService = eval(input('What type of cleaning service do you want? \n  1-Floor Cleaning \n  2-Bathroom \n'))


   #prompt for number of rooms needing sercice
    numRooms = eval(input('how many rooms are you needing service here? \t'))

   #validate cService input
    if(cService <= 0 or cService > 2):
        print("Please choose a service number that's avalible?")
        cService = eval(input('What type of cleaning service do you want? \n  1-floor cleaning \n  2-bathroom'))
        
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

    #validate number of rooms input
    if(numRooms <= 0):
        print('Please enter a valid room number count')
        numRooms = eval(input('how many rooms are you needing service here? \t'))



    #calclulation for total cost
    totalCost = numRooms * serviceCost
   
    #print service total cost
    print('Your total cost: ',totalCost)




#run program
main()

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

