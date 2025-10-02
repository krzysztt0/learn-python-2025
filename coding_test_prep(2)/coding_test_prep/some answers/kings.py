def next_king(name):
    parts = name.split()

    first_name = parts[0]
    number = int(parts[1])   # if it's not a number, this will crash

    if first_name == "Christian":
        return f"Frederick {number + 1}"
    elif first_name == "Frederick":
        return f"Christian {number}"