#Name:Imani Cornelius
#Date: 11/18/24
#Descri: Strings and files practice problem

#Algorithm
#Read and store data from customer's account including: Account number, Beginning balance, withdrawals and deposits.
#Tell user to enter his/her name and age.
#Then convert the customers name to a username which will then consits of the first letter of the first name, last name(5 digits) and age.
#The account number should then be in the following format: XXX-XX-XXX.
#Calculate total of deposits,withdrawals, and ending balance in the account.
#Then display users report to both screen & file called "JanuaryStatement.txt".

print("Welcome to my string and file's program!")
print("This program will store and read data from the file called january.txt.")
print("The program will include the customer account number, balance, withdraws, and deposits.")
print("The program will then convert the user's information and convert the account number to the format:XXX-XX-XX.")
print(" Then the total deposits, withdrawals and ending balance will be calculated.")
print("The program will then display a report to both the screen and file.")

import os # function for file,variable and commands

# Create the input file if it doesn't exist

with open("November.txt", "w") as file:
    
    file.write("123456789\n")
    
    file.write("1000.00\n")
    
    file.write("250.00\n")
    
    file.write("500.00\n")
    

def format_account(account_num):
    
    acc = str(account_num)
    
    return f"{acc[:3]}-{acc[3:5]}-{acc[5:]}"

def create_username(first_name, last_name, age): #Get information from user
    
    return (first_name[0] + last_name[:5] + str(age)).lower()

def process_statement():
    
    name = input("Enter your full name (First Last): ") # Get user input
    
    age = int(input("Enter your age: "))
    
    first_name, last_name = name.split()  # Split name into first and  last 
    username = create_username(first_name, last_name, age)
    
    if os.path.exists("November.txt"): # Check file exists and read data
        
        infile = open("November.txt", "r")
        
        account_num = infile.readline().strip()
        
        beginning_balance = float(infile.readline())
        
        withdrawals = float(infile.readline())
        
        deposits = float(infile.readline())
        
        infile.close()
    else:
        print("Input file 'November.txt' not found. Creating sample data.")
        
        account_num = "123456789" # Sample data if file doesn't exist

        beginning_balance = 1000.00
        
        withdrawals = 250.00
        
        deposits = 500.00
        
    ending_balance = beginning_balance - withdrawals + deposits # Calculate ending balance 
    
    formatted_account = format_account(account_num) # Format for account number 
    
    # Statement with column format
    
    statement = f"""

{'Customer Name':<20} {'Username':<15} {'Account Number':<15}

{'-'*20:<20} {'-'*15:<15} {'-'*15:<15}

{name:<20} {username:<15} {formatted_account:<15}

{'Transaction Type':<20} {'Amount':<15}

{'-'*20:<20} {'-'*15:<15}

{'Beginning Balance:':<20} ${beginning_balance:>14,.2f}

{'Total Withdrawals:':<20} ${withdrawals:>14,.2f}

{'Total Deposits:':<20} ${deposits:>14,.2f}

{'Ending Balance:':<20} ${ending_balance:>14,.2f}
"""
    
    print(statement)
    
    outfile = open("NovemberStatement.txt", "w")
    
    outfile.write(statement) 
    outfile.close()
    
    print("Thank you for using my program!")

if __name__ == "__main__":
    process_statement()


