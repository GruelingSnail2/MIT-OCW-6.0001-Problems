#House Hunting
#Calculate how much to save per month to reach goal in certain amount of time

#Ask for user inputs as floats
annual_salary=float(input("Enter your annual salary: "))

#Initialize variables
x=annual_salary #used to reset annual salary later
total_cost=1000000
portion_down_payment = 0.25
current_savings=0.0
r=0.04
num_months=0
total_months=36
semi_annual_raise=0.07
monthly_saved=0

#initialize variables for bisection search
high=1
low=0
portion_saved_guess=(high+low)/2
num_guesses=0
epsilon=100 #how far from goal is acceptable

#Beginning calculations
monthly_salary=annual_salary/12
down_payment=total_cost*portion_down_payment
investment=current_savings*(r/12)
monthly_saved=portion_saved_guess*monthly_salary

#bisection search for savings rate based on 36 month timeline

while True:
    portion_saved_guess=(high+low)/2
    while num_months<total_months:
        current_savings=(portion_saved_guess*monthly_salary)+investment+current_savings
        if num_months%6==0: #adjust for semi-annual raise given by user input
            annual_salary=annual_salary+semi_annual_raise*annual_salary
            monthly_salary=annual_salary/12
        investment=current_savings*(r/12)
        num_months+=1
    num_months=0
    
    if abs(current_savings-down_payment)<=epsilon:
        print("Best savings rate: ", portion_saved_guess)
        print("Steps in bisection search: ", num_guesses)
        break
    elif abs(current_savings-down_payment)>=epsilon and current_savings<down_payment:
        low=portion_saved_guess #adjust guess that was too low by moving lower bound up
    elif abs(current_savings-down_payment)>=epsilon and current_savings>down_payment:
        high=portion_saved_guess #adjust guess that was too high by decreasing upper bound
    if low==high: #no answer possible
        print("It is not possible to pay the down payment in three years.")
        break
    current_savings=0
    num_guesses+=1
    annual_salary=x
    
    