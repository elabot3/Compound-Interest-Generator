# Compound-Interest-Generator


Compound Interest with Loops

I am sure you recall the Chapter 2 Compound Interest assignment.  You coded a program using the formula below to compute what the money will be worth at the end of the term.   A sample output solution is given below.  

FV = PV (1 + r\m)**mt

Compound interest arises when interest is added to the principal, so that from that moment on, the interest that has been added also itself earns interest. This addition of interest to the principal is called compounding. A bank account, for example, may have its interest compounded every year: in this case, an account with $1000 initial principal and 20% interest per year would have a balance of $1200 at the end of the first year, $1440 at the end of the second year, and so on.  Read more at: http://en.wikipedia.org/wiki/Interest_compounded

You will create a Python program that allows for the numeric entry of Deposit, Interest Rate Percentage and Number of Months.  You will calculate the interest for each month the deposit is to be in the saving account. 

The power of compounded interest is your money will grow faster.  For this assignment you will be coding a special feature to determine how many months it will take for your original investment to reach your saving goal.

Coding Requirements:
1. Prompt the user for these required input values:  Deposit, Interest Rate Percentage and Number of Months, and Goal. Make sure to select the appropriate data type for each. 

2. Perform data validation on the Deposit, Interest Rate Percentage and Number of Months, and Goal are numeric using Python error handling which can be found in Blackboard.  Use Python’s loops to accomplish the three sub-tasks below:
If the contents are not numeric issue a message and prompt them again until the user enters a valid number for each of the input variables.  
Make sure Deposit, Interest Rate Percentage and Number of Month are non-zero and positive values or issue an error message and ask for input again.  
The Goal amount can be 0 but not negative.  If negative issue an error message and ask for input again.  

3. Convert Interest Rate Percentage inputted value to a decimal variable and then divide the  interest rate decimal value by 12 to get a monthly interest rate.   For example 0.04 / 12 = 0.0033. This newly computed value is the Monthly Interest Rate.

4. Code a loop to execute up to the Number of Months variable value the user has supplied to compound the interest rate.  You can choose a while or for loop. 
Multiply the Deposit by the Monthly Interest Rate that was determined above to get the interest for the month. 
Add the interest for the month to the Deposit to get the new Account Balance
Output the Month Number and the new Account Balance (formatted as currency) to the screen
Repeat the loop until the number of months has been met.

5. Code another loop to predict how many months it will take of compounding to reach your Goal amount.  Note: You shouldn’t use a for loop because you don’t know how many months it will take):
Keep track of how many times you are through the loop.  This will represent the number of months to reach your goal.
Use the same logic you coded in Step 4 to compute each month’s Compounded Savings Account balance but do not output anything at this point. 
Compare the Compounded Savings Account to what the Goal is.  Keep executing if the Compounded Savings Account is less than the Goal amount.
Once you reach the Goal amount format the number of months with thousands separator and output the results.

6. Make sure you use Hungarian Notation when naming the variables.
7. Make sure to include comments in your code.
