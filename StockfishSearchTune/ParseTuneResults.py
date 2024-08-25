def parse_tune_results(file):
    # returns an array of tuples (param, value, original_value)
    with open(file, 'r') as f:
        lines = f.readlines()
        
    results = []
    
    for line in lines:
        line = line.strip().split()
        
        if len(line) <= 1:
            print("Skipping line: ", line)
            continue
        try:
            line[1] = round(float(line[1]))
            line[2] = int(line[2])
        except:
            print("Error during conversion: ", line)
            continue
        results.append((line[0], line[1], line[2]))
        
    return results

