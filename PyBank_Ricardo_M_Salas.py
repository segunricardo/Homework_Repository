# PyBank Code

import os
import csv

# telling the computer about path to dataset
csvpath = os.path.join("budget_data.csv")
with open(csvpath, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader, None) # Command to skip first row of information

    months = 0 # creates a variable to count the months
    profits = 0 # creates a variable to add profits & losses
    
    profits_ls = [] # defines a list to retreieve profits
    months_ls = [] # define a list to retrieve months
    for row in csvreader: #Create a loop to go through the whole spreadsheet vertically.
        months = months + 1 # compile number of months from the file
        months_ls.append(row[0]) # Add number of months in list

        profits = profits+int(row[1]) # this commans will add up whole profits in column 2 (profits)
        profits_ls.append(row[1]) # This creates a list to store profits/losses, also in relation to column 2. 
print("total profits: " + str(profits)) #Important to put as string, since print cannot output integers!

# We want to check for average changes in "Profit/Losses" over entire timeframe, so:

var_ls= [0] # creates a variable for storing monthly variations in profits
var = 0 #  Creates a variable to deposit monthly variations in profits

for i in range(len(profits_ls)-1): # looping first through profits
    var = int(profits_ls[i+1])-int(profits_ls[i]) # then subtracting previous month's profits to calculate monthly variations
    var_ls.append(var) # Adds all values from monthly vriations to list

var_average=sum(var_ls)/len(var_ls) # calculates average monthly change in profits
print("Average monthly variation in profits: " + str(round(var_average, 2))) #Again, important to put as string, since print cannot output integers!


# Finding out the months of greatest losses and profits over entire timeframe
var_greatest=0 
var_lowest=0

for i in range(len(var_ls)-1): # this loop searches through list of monthly variations in profits
    if var_ls[i] > var_greatest : # this line replaces value of variable for greatest change each time a higher value is found
        var_greatest = var_ls[i]  
    if var_ls[i] < var_lowest : # this line replaces value of variable for lowest change each time a lower value is found
        var_lowest=var_ls[i]

dict_var = dict(zip(months_ls, var_ls)) # this command compiles a list with monthly changes in profits into a dictionary

print("lowest variation: "+str(var_lowest) + ", highest variation: " + str(var_greatest))

for month, extremes in dict_var.items(): # this loop searches through the dictionary for the month of the highest and lowest values!
    if extremes == var_greatest:
        month_greatest =  month
        print("Greatest positive variation: " + month_greatest )
    if extremes==var_lowest:
        month_lowest = month
        print("Greatest negative variation: " + month_lowest ) 


    #Creating a .txt file

    file = open("Financial_Report.txt","w") 

file.write("Financial Analysis\n")
file.write("-----------------------\n")
file.write("Total Months: " + str(months) + "\n")
file.write("Total profits: " + str(profits) + "\n")
file.write("Average Variation: $"+ str(round(var_average,2))+ "\n")
file.write("Greatest positive variation: " + str(var_greatest) + " (" + str(month_greatest) + ")\n" )
file.write("Greatest negative variation: " + str(var_lowest) + "(" + str(month_lowest) + ")\n" )

file.close()