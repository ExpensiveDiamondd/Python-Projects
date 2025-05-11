print("Welcome to my leap year program!")
print("This program will determine if a year is a leap year or not")
print("The program will then display the leap year.")

"""
Algorithm
determine if a year is a leap year by entering year between 1900 and 100000. 
if true, return the boolean true,otherwise return false. 
"""

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

for year in range(2057,2061):
    
    year = int(input("Enter a year:"))

    if is_leap_year(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
    
