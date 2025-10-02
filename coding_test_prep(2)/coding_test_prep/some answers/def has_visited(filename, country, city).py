def has_visited(filename, country, city):
    with open(filename, 'r') as file:
        for line in file:
            # Remove whitespace and newline
            line = line.strip()
            if not line:
                continue
            
            # Split country and city
            parts = line.split(',')
            if len(parts) != 2:
                continue  # skip malformed lines
            
            file_country, file_city = parts[0].strip(), parts[1].strip()
            
            if file_country == country and file_city == city:
                return True
    
    return False