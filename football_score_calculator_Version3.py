# Football Score Calculator
team1 = input("Enter Team 1 name: ").strip()
team2 = input("Enter Team 2 name: ").strip()

# Validate team names aren't empty
while not team1 or not team2:
    print("Team names cannot be empty!")
    team1 = input("Enter Team 1 name: ").strip()
    team2 = input("Enter Team 2 name: ").strip()

team1_goals = 0
team2_goals = 0
time = 0

while True:
    event = input("\nEnter '1' if Team 1 scores, '2' if Team 2 scores, 't' to add time, 'q' to quit: ")

    if event == 'q':
        break
    elif event == '1':
        team1_goals += 1
        print(f"Goal! {team1} scores")
    elif event == '2':
        team2_goals += 1
        print(f"Goal! {team2} scores")
    elif event == 't':
        try:
            minutes = int(input("Enter minutes passed: "))
            if minutes < 0:
                print("Minutes cannot be negative!")
            else:
                time += minutes
                print(f"Time updated: {time} minutes")
        except ValueError:
            print("Please enter a valid number!")
    else:
        print("Invalid input!")

# Final Score
print("\n" + "="*40)
print("FINAL SCORE")
print("="*40)
print(f"{team1}: {team1_goals}")
print(f"{team2}: {team2_goals}")
print(f"Match Time: {time} minutes")

# Determine winner
if team1_goals > team2_goals:
    print(f"\n {team1} wins!")
elif team2_goals > team1_goals:
    print(f"\n {team2} wins!")
else:
    print("\n It's a draw!")
print("="*40)
