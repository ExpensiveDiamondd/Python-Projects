"""
Alogrithm
Tell user to to inout their name, age, and email address for 4 individuals
The program should store the information in a file called user_data.txt
Display Output of 4 individuals information
"""
 #Intro
print("Welcome to my files program!")
print("This program will tell the user to input their age,name and email address info for 4 individuals.")
print("This program will then store the information using a file called user_data.txt")
print("This program will then display all information of the 4 individuals")

def add_file_header(f):
    header = "+" + "-" * 20 + "+" + "-" * 7 + "+" + "-" * 27 + "+\n"
    f.write(header)
    f.write("| {:<18} | {:<5} | {:<25} |\n".format("name", "age", "email"))
    f.write("+" + "-" * 20 + "+" + "-" * 7 + "+" + "-" * 27 + "+\n")

def collect_user_data():
    with open('user_data.txt', 'w') as f:
        add_file_header(f)
        
        for i in range(4):
            print("\nEnter details for person", i+1)
            name = input("Name: ")
            age = input("Age: ")
            email_address = input("Email: ")
            
            f.write("| {:<18} | {:<5} | {:<25} |\n".format(name, age, email_address))
            f.write("+" + "-" * 20 + "+" + "-" * 7 + "+" + "-" * 27 + "+\n")

    # Read and display the file contents
    with open('user_data.txt', 'r') as f:
        file_contents = f.read()
        print("\nHere are the contents of your file:")
        print(file_contents)

    print("User data has been saved to 'user_data.txt'.")

def main():
    collect_user_data()
    print("\nThank you for using my file program!!")

if __name__ == "__main__":
    main()

