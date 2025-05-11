#Algorithm

#Tell user to enter a 10- character telephone number in the format XXX-XXX-XXXX
#Then the application should display the telephone number with any alphabetic character's,
#which should appear in the original translated to their numberic equivalent.
#If user enters 555-GET-FOOD, the application should display as 555-438-3663.

#Introduction
print(" Welcome to my telephone program")
print("This program will tell the user to enter a 10- character telephone number in the format of XXX-XXX-XXXX")
print("Then the program should display the telephone number with the alphabetic character's below, which should appear as their original translated numeric equivalent.")

def letter_to_number(letter):
    phone_letters = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }
    return phone_letters.get(letter.upper(), letter)

def convert_phone_number():
    print("Enter a 10-character telephone number in the format XXX-XXX-XXXX:")
    phone = input()
    
    converted = ''
    for char in phone:
        converted += letter_to_number(char)
    
    print(f"Converted number: {converted}")
    print("\nThank you for using my telephone program!")
if __name__ == "__main__":
    convert_phone_number()
