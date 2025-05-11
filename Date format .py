#Algorthm
#Tell user to create a string that contains a date format
#Print the date in the format of mm/dd/yyyy
#Display result

#intro
print("Hello, welcome to my program!")
print("This program will tell the user to create a string that contains a date format")
print("The program will display the results of that date.")

def format_date(date_input):
    month,day, year = date_input.split('/')
    months = ['January','February','March','April','May','June','July','August','September','October','November','December',]
    month_name = months [int(month) -1]
    day = str(int(day))
    return f" {month_name} {day},{year}" 

def main():
    format_date = str(input)("Enter date:")("mm/dd/yyyy:")
    result = format_date()
    print(result)
    print("\n Thank you for using my date format program!!")
         
if __name__ == "__main__":  
    main()
    
    
    
    
