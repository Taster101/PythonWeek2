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

#print total pay
    print('total pay:  \t' ,totalPay)

main()
