#This this program is for cleaning services that takes user input for number of small and large rooms, then decides the type of service to deliver final total

def main():
#prompt for first number
    num1 = eval(input('How many large rooms do you have?'))

#prompt for second number
    num2 = eval(input('How many large rooms do you have?'))

#prompt for math operation
    operator = input('What type of service are you looking for today?    \n "-" regular no repeat service \n "+" for speedy service here  \n "*" - for repeated serive '  )

#intailize room prices
    sRoom = 30
    lRoom = 70

#intialize speedy service cost
    speedyService = 50

#if statement for total price
    if(operator == '+'):
           totalPrice    = (num1 * sRoom) + (num2 * lRoom) + speedyService                                     #total price with speedy service

    elif(operator == '-'):
            totalPrice  = num1 * sRoom + num2 * lRoom                                                  #total pprice for regular service
            
    elif(operator == '*'):
            repService = eval(input('What is the number of repeats you want to schule'))                        # prompt for repeated service count
            totalPrice  = (num1 * sRoom) + (num2 * lRoom) * repService                                        #totalPrice for repeat service



    #print totalPrice
    print('Your total price is: \t ',totalPrice)

main()
