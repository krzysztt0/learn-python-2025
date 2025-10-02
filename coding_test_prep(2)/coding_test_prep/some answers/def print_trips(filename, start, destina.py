def print_trips(filename, start, destination):
    trips = []
    total_delay = 0
    
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) != 3:
                continue  # skip malformed lines
            trip_start, trip_dest, delay_str = parts
            if trip_start == start and trip_dest == destination:
                delay = int(delay_str)
                trips.append((trip_start, trip_dest, delay))
                total_delay += delay
                print(line.strip())
    
    if trips:
        average_delay = total_delay // len(trips)
        print("Average delay:", average_delay)
    else:
        print("No trip found.")