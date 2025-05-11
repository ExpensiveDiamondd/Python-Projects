def main():
 """
Algorithm
Enter grades in each class
calculate by adding each grade
after adding each grade then divide by the given number
display average of entered grades average until you get a negative number.
 """
print("Enter Grades earned in 4 subjects") 
Sum = 0
count = 0
grade = 0 
while grade >= 0:

  grade = int(input("What is the first grade?"))
  if grade >= 0:
     Sum = Sum + grade
     count = count + 1 
     print (Sum) 
print(" out of the loop" ,Sum )
