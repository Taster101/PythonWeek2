print('Name Ryan Fox')

print('Class: CMSC 105')

print('Date: 20 January 2024')

print('This program will use user dimensions of wood needed and total cost of wood.')

#Set cost of wood per square foot.

wood = 1.34

#Ask for user input of the length and width of wood needed.

length = float(input('How many inches long?'))
width = float(input('How many inches wide?'))
quanity = eval(input('How many would you like ?')) # added prompt to get quainty

# Equation to result square footage.

square_foot = quanity * length * width / 144  #added quainty to square_foot caculation

#Equation for total cost.

total = square_foot * wood


#Print total square foot and total cost using math equations.

print('Total square feet: ', square_foot)
print('Total cost: $', total)






