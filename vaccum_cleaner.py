def agent(percept):
    room, status = percept
    if room == "A":
        if status == "Clean":
            return "Move to right"
        else:
            return "Suck"
    if room == "B":
        if status == "Clean":
            return "Move to left"
        else:
            return "Suck"

rooms = ['A', 'B']
clean_status = ['Clean', 'Dirty']
percept_table = {}

while True:
    room = input("enter the room A or B or Q to quit: ")
    if room.upper() == 'Q':
        break
    status = input("enter clean or dirty: ")
    

    room = room.upper()
    status = status.capitalize()
    if room not in rooms or status not in clean_status:
        print("Invalid input enter again")
        continue
    percept = (room, status)
    action = agent(percept)
    percept_table[percept] = action
    print("action: ", action)
print("Agent \t\t Status \t\t P-A table")
for percept, action in percept_table.items():
    print(f"{percept[0]} \t\t {percept[1]} \t\t {action}")