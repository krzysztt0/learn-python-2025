def next_king(name):
    # Split the input into king and number (if any)
    parts = name.split()
    
    # Handle the case with a number
    if len(parts) == 2:
        king, number = parts[0], int(parts[1])
        if king == "Christian":
            return f"Frederick {number}"
        else:  # king == "Frederick"
            return f"Christian {number + 1}"