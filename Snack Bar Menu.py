# Name: ImaniCornelius
# Date:10/24/24
# Descr: SnackBarMenu 

#Snack Bar Menu


#Introduction
print("Welcome to my Snack Bar menu Program!")
print("This program will allow the user to choose from the menu until the user chooses to exit.")
print("This program will keep running the total of the charges.")
print("The program will then add the 7% to calculate the final bill and then dispay total to user.")


                            #Algorithm 
# Ask user to choose from following menu 1-5 until user chooses to exit.
# Use constants to store each price of item from menu. 
# The program will then add 7% sales tax to calculate the final bill.
# Display the total the user.

# Constants
BURGER_AND_FRIES_PRICE = 10.25
HOT_DOG_PRICE = 4.25
NACHO_CHEESE = 7.50
TENDERS_AND_FRIES = 6.25
PRETZEL_WITH_CHEESE = 5.25
TAX_RATE = 0.07 # 7% Tax rate

# Constants for item prices
BURGER_FRIES_PRICE = 10.25
HOT_DOG_PRICE = 4.25
NACHO_CHEESE_PRICE = 7.50
TENDER_FRIES_PRICE = 6.25
PRETZEL_CHEESE_PRICE = 5.25

# Menu constants to item names
menu = {
    1: ("Burger_Fries", BURGER_FRIES_PRICE),
    2: ("Hot_Dog", HOT_DOG_PRICE),
    3: ("Nacho_Cheese", NACHO_CHEESE_PRICE),
    4: ("Tender_Fries", TENDER_FRIES_PRICE),
    5: ("Pretzel_Cheese", PRETZEL_CHEESE_PRICE)
}

def display_menu():
    print("\nSnack Bar Menu:")
    for key, value in menu.items():
        print(f"{key}. {value[0]} - ${value[1]:.2f}")

def main():
    subtotal = 0

    while True:
        display_menu()
        choice = input("Please choose an item from menu (1-5) or type 'exit' to quit: ")

        if choice.lower() == 'exit':
            break  # Exit the loop when the user types 'exit'

        if choice.isdigit():
            choice_num = int(choice)
            if choice_num in menu:
                item_name, item_price = menu[choice_num]
                subtotal += item_price
                print(f"You added {item_name}. Current subtotal: ${subtotal:.2f}")
            else:
                print("Error: Please choose a valid number between 1 and 5.")
        else:
            print("Error: Invalid input. Please enter a number between 1 and 5 or 'exit' to quit.")

    # Display subtotal without tax
    print(f"\nSubtotal without tax: ${subtotal:.2f}")

    # Tax Calculation and Grand Total
    TAX_RATE = 0.07
    tax_amount = subtotal * TAX_RATE
    grand_total = subtotal + tax_amount

    # Display the tax and final total
    print(f"Tax (7%): ${tax_amount:.2f}")
    print(f"Grand Total: ${grand_total:.2f}")

    # Thank-you message
    print("\nThank you for ordering from the snack bar!")
    print("Have a great day!!")

if __name__ == "__main__":
    main()
