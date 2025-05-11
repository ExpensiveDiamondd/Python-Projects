def main():

#Introduction    
#A bug collector collects bugs every day for seven days. Write a program that keeps a running,total of the mumber of bugs collected during the sevenn days. The loop should ask
#for the number of bugs collected for each day, and when the loop is finished, the program should display the total number of bugs collected.

  set_total= 0

 #for each day of 7 days:
    #input bugs collected for a day
    #Add bugs collected to total

    #Display to

#Initialize the accumulator
  total = 0

#Get bugs collected for each day.

for day in range(1 , 8):
   print('Enter thr bugs collected on day,',day)
   
#Input the number of bugs. 
   bugs = int(input())
   
#Add bugs to total 
   total += bugs


#Display the total bugs.

print('You collected a total of',total,'bugs,')
