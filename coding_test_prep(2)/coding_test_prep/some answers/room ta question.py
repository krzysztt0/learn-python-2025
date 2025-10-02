def check_ta_count(rooms,tas):
    if rooms<=tas:
        print("Thank you very much for such a generous support.")
    else:
        print("Unfortunately, I need more TAs to run the exercise sessions.")
check_ta_count(11,11)



def assign_tas(rooms,tas):
    for ta in range(1, tas+1):
        room=((ta-1)% rooms) +1
        print(f'TA{ta} goes to room {room}.')

