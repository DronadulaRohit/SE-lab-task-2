goal_state = {'A': '0', 'B': '0'}

def vacuum_agent(loc, status_A, status_B):
    actions = []
    cost = 0

    if loc == "A":
        if status_A == '1':     # If A dirty, clean it
            actions.append("Suck")
            status_A = '0'
            cost += 1
        if status_B == '1':     # If B dirty, move & clean
            actions.append("Move Right")
            actions.append("Suck")
            status_B = '0'
            cost += 2

    elif loc == "B":
        if status_B == '1':     # If B dirty, clean it
            actions.append("Suck")
            status_B = '0'
            cost += 1
        if status_A == '1':     # If A dirty, move & clean
            actions.append("Move Left")
            actions.append("Suck")
            status_A = '0'
            cost += 2

    return actions, cost

# Input
location = input("Enter the initial position of VC (A/B): ")
status_A = input("Enter status of A (0-clean / 1-dirty): ")
status_B = input("Enter status of B (0-clean / 1-dirty): ")

# Run agent
actions, total_cost = vacuum_agent(location, status_A, status_B)

# Output
print("\nActions:")
for i in actions:
    print(i)
print("Total Cost:", total_cost)
