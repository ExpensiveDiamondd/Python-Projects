#Name: Imani Cornelius
#Date: 11/29/24
#Descri: Old Mac Donald song program

#Algorithm
#Write a program to print the lyrics of the song Old MacDonald.

#This program will include the lyrics for five different animals.

#This program will use function and use parameters for the animal and the sound.

#Introduction
print("Welcome to my Old MacDonald Song program!")

print("This program will include the lyrics for five different animals.")

print("This program will use functions and parameters for the animal and the sound.")

def sing_verse(animal, sound):
    
    print(f"Old MacDonald had a farm, E-I-E-I-O")
    
    print(f"And on that farm he had a {animal}, E-I-E-I-O")
    
    print(f"With a {sound} {sound} here")
    
    print(f"And a {sound} {sound} there")
    
    print(f"Here a {sound}, there a {sound}")
    
    print(f"Everywhere a {sound} {sound}")
    print()

def main():
    # List of tuples containing (animal, sound)
    
    farm_animals = [
        
        ("Pig", "oink"),
        ("Sheep", "baa"),
        ("Horse", "neigh"),
        ("Goat", "maa"),
        ("Cow", "moo")
    ]
    
    # Iterate through the animals and sing each verse
    
    for animal, sound in farm_animals:
        
        sing_verse(animal, sound)
        
        print("Thank you for using my program!")
        
if __name__ == "__main__":
    main()
