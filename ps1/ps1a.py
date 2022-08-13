#House Hunting
#Calculate number of months it will take to save for a down payment on a house given variables

#Ask for user inputs as floats
annual_salary=float(input("Enter your annual salary: "))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost=float(input("Enter the cost of your dream home: "))

#Initialize variables
portion_down_payment = 0.25
current_savings=0.0
r=0.04
monthly_salary=annual_salary/12
total_months=0

#Beginning calculations
portion_down_payment=portion_down_payment*total_cost
monthly_saved=portion_saved*monthly_salary

#Find the total number of months needed to save for the down payment
while current_savings<=portion_down_payment: 
    investment=current_savings*(r/12)
    current_savings=monthly_saved+investment+current_savings
    total_months+=1

#display results
print ("Number of months: ",total_months)

