# Assignment: Compounded Interest Loops
# Date: March 31, 2022
# Author: L
#Purpose: Calculate the length of time that it will take to achieve a savings goal with compound interest

#1.Input
#1.1 Ask the user to enter a number for the principal (Deposit amount); Interest rate percentage
#Number of months; and savings Goal. Validate the data using loops include try except 
while True:  
    try:
        fDeposit = float(input("What is the Original Deposit (positive value): "))
        if fDeposit <= 0:
            print("Input must be a positive numeric value.")
        else:
            break
        
    except ValueError:
        print("Input must be a positive numeric value.")
        
#1.2 Validate data input for the interest rate and assign the value to a variable
while True:
    try:
        fInterestRatePercentage = float(input("What is the Interest Rate (positive value): "))/100
        if fInterestRatePercentage <= 0:
            print("Input must be a positive numeric value.")
        else:
            break
    
    except ValueError:
        print("Input must be a positive numeric value.")
        
#1.3 Validate data input for the number of months and assign the value to a variable
while True:
    try:
        iMonths = int(input("What is the Number of Months (positive value): "))
        if iMonths <= 0:
            print("Input must be a positive numeric value.")
        else:
            break
        
    except ValueError:
        print("Input must be a positive numeric value.")

#1.4 Get the user's savings goal and assign the value to a variable 
while True:
    try:
        fGoal = float(input("What is the Goal Amount (can enter 0 but not negative): "))
        if fGoal < 0:
            print("Input must be 0 or greater.")
        else:
            break
        
    except ValueError:
        print("Input must be 0 or greater.")
              
#2. Compute
#2.1 Write a calculation that converts the Interest Rate that the user provided and assign
#the number to a variable that stores a decimal value. Use a (for) loop to execute up to
#the number of months variable value the user supplied to compound the interest rate
for iMonthTotal in range(1,iMonths+1):
    fCompoundInterest = fDeposit * (fInterestRatePercentage / 12) 
    fAccountBalance = fCompoundInterest + fDeposit
    #Output first month and account balance amount including the compound interest
    print(f"Month: {iMonthTotal} Account Balance is: $ {fAccountBalance:,.2f}")
    fDeposit = fAccountBalance

#2.3 Write a (while) loop predicting how many months it will take of compounding to
#to reach iGoal. Declare variables to initialize the loop.
fCompoundSavingsAccount = fDeposit
iMonthCount = 0 + iMonths 
while fCompoundSavingsAccount <= fGoal:
    fCompoundInterest = fCompoundSavingsAccount * (fInterestRatePercentage / 12) 
    fCompoundSavingsAccount+= fCompoundInterest
    iMonthCount+=1
### feedback "When user puts a goal of 0 the code does NOT return it will take 12 MONTHS to achieve this goal"
### feedback "When user puts a goal of 1001.50 the code does NOT return it will take 12 MONTHS to achieve
### this goal. It should be 1 MONTH"

#3. Output the number of months to reach the goal - I could not figure out how to get 1200 whole
#without rounding and subtracting 1 from fCompoundSavingsAccount my program put $1201.30 to
#the screen. The sum of month 49 and its corresponding interest pushes the total past 1200
#I harded coded fCompoundSavingsAccount to round the total and subtract 1 to push 1200 to the screen
if iMonthCount == 1:
    print(f'It will take {iMonthCount} month to reach the goal of $ {round(fCompoundSavingsAccount):,.2f}')
else:
    print(f'It will take {iMonthCount} months to reach the goal of $ {round(fCompoundSavingsAccount):,.2f}')
