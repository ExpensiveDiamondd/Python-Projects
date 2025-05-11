#Algorthim
#Tell user to enter a player's score for 7 days of each week
#Calculate player's average score for the week
#Display how many scores were above the average.

def analyze_scores():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    scores = []
    
    # Get scores for each day
    for i in range(7):
        print(f"Enter score for {days[i]}: ")
        score = int(input())
        scores.append(score)
        
    # Calculate Average         
    average = sum(scores)/len(scores)

    # Count scores above average
    above_average = 0
    for score in scores:
        if score > average: 
            above_average += 1

    # Display results
    print(f"\nWeekly average score: {average:.2f}")
    print(f"Number of days above average: {above_average}")

    # Days that were above average
    print("\nDays above average:")
    for i, score in enumerate(scores):
        if score > average:
            print(f"{days[i]}: {score}")

print("Weekly Player Score Tracker")
analyze_scores()

