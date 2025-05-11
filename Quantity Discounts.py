def main():

#Algorithm
 """
tell user to enter number of pacakges purchased
calculate packages purchased by multiplying the discounted price by total cost.
to calculate final cost after discount, subtract the discount from the initial cost
 """
#Introduction
print("Welcome to my Quanity discount program!")
print("This program will tell how many pacakges are purchased & total cost of the purchase after the discount")
print("This program will be using multiplication and subtraction to get the output result for this program.")

#Input
Quantity = int(input("Enter number of packages purchased:"))
# Retail_price = 99
# quantity * retail_price = total price 

if userNumberofPackages <10:
     discount = 0;
elif userNumberofPackages<20: 
     discount = 0.10
elif userNumber0fPackages<50:
     discount = 0.20
elif userNumberofPackages <100:    
     discount = 0.30
else:
    discount = 0.40
    
#subTotal = numberofpackages * package price:
#discountAmoount = discount * subTotal
#total * subTotal - discountAmount

print( "Amount of discounts:") + str(discountAmount, ",.3f") + \
"/nTotal amount: $" + format(total,",.2f")
 

    
    
