def check_ta_count(rooms,tas):
    if rooms <= tas:
        print("Thank you very much for such a generous support.")
    else:
            print("Unfortunately, I need more TAs to run the exercise sessions.")
    



def assign_tas(rooms,tas):
    if num_tas < num_rooms:
        print("Error: Not enough TAs for the rooms.")
        return
    
    for room in range(1,rooms +1):
        print(f"TA {room} goes to room {room}.")

    for ta in range(num_rooms + 1, num_tas + 1):
        room = num_rooms  # could be any room
        print(f"TA {ta} goes to room {room}.")

