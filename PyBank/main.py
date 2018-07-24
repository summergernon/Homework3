# PyBank Homework

# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('Resources', 'budget_data_1.csv')

# Open the file
with open(csvpath, newline='') as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')

    # Skip headers
    next(csvreader,None)

    # Set initial variables
    revenue = []
    date = []
    revenueChange = []

# Sum the first column to come up with number of months and the second column to get total revenue
    for row in csvreader:
        revenue.append(float(row[1]))
        date.append(row[0])

    # Print the header and totals for months and revenue
    print('Financial Analysis')
    print('----------------------------')
    print('Total Months:  ', len(date))
    print('Total Revenue:  $', sum(revenue))

    # Find the difference between the revenue totals and take that divided by the length of revenue change
    for i in range(1,len(revenue)):
        revenueChange.append(revenue[i] - revenue[i-1])
        avgrevenueChange = sum(revenueChange)/len(revenueChange)

        # Find the greatest increase in revenue & its date
        maxrevenueChange = max(revenueChange)
        maxrevenueChangedate = str(date[revenueChange.index(max(revenueChange))])

        # Find the greatest decrease in revenue & its date
        minrevenueChange = min(revenueChange)
        minrevenueChangedate = str(date[revenueChange.index(min(revenueChange))])

    # Print these results
    print('Average Revenue Change:  $', avgrevenueChange)
    print('Greatest Increase in Revenue', maxrevenueChangedate, '($', maxrevenueChange, ')')
    print('Greatest Decrease in Revenue: ', minrevenueChangedate, '($', minrevenueChange, ')')

        
