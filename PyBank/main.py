# import modules
import csv
import os

#path to collect data
fileLoad = os.path.join("Resources", "budget_data.csv")

#file to hold the output
outputfile = os.path.join("Analysis.txt")
#find total months
#set up variables and initialize to 0
totalMonths = 0 
netTotal = 0
monthlyChanges = []
months =[]

#read the csv file
with open(fileLoad)as revenueData:
    #create a csv reader object
    csvreader = csv.reader(revenueData)

    #read the header row
    header = next(csvreader)
    #move to the first row
    firstRow = next(csvreader)
    
    totalMonths += 1
    
    netTotal += float(firstRow[1])
    #establish the previous amount
    previousAmount = float(firstRow[1])
    #increment the count of the total months


    for row in csvreader:
        totalMonths += 1
        #track the net total amount of Profit/Losses
        netTotal += float(row[1])
        #calculate the net change
        netChange = float(row[1]) - previousAmount
        #add on to the list
        monthlyChanges.append(netChange)
        #add the first month that a change occured, month is in index 0
        months.append(row[0])
        #update the previous revenue
        previousAmount = float(row[1])

#calculate the average
averageChange = sum(monthlyChanges) / len(monthlyChanges)

greatestIncrease = [months[0], monthlyChanges[0]]
greatestDecrease = [months[0], monthlyChanges[0]]
#use loop to calculate the index of the greatest and least change
for m in range(len(monthlyChanges)):
    #calculate the greatest increase and decrease
    if (monthlyChanges[m] > greatestIncrease[1]):
        greatestIncrease[1] = monthlyChanges[m]
        #update the month
        greatestIncrease[0] = months[m]

    if (monthlyChanges[m] < greatestDecrease[1]):
        greatestDecrease[1] = monthlyChanges[m]
        #update the month
        greatestDecrease[0] = months[m]


output = (
    f"Financial Analysis \n"
    f"---------------------- \n"
    f"Total Months:  {totalMonths}\n"
    f"Total: ${netTotal:,.2f}\n"
    f"Average Change: ${averageChange:,.2f}\n"
    f"Greatest Increase: {greatestIncrease[0]} Amount ${greatestIncrease[1]:,.2f}\n"
    f"Greatest Decrease: {greatestDecrease[0]} Amount ${greatestDecrease[1]:,.2f}\n"
    )
print(output)

#export the output to the text file
with open(outputfile, "w") as textfile:
    textfile.write(output)


