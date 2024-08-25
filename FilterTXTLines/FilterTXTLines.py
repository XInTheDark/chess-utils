# given a file name, filter away every line that does not contain all the strings in a list

def filterTXTLines(file_name, strings):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    filtered_lines = [line for line in lines if all(string in line for string in strings)]
    
    # write to file
    with open(file_name, 'w') as file:
        for line in filtered_lines:
            file.write(line)
            

if __name__ == "__main__":
    filterTXTLines('pgn2.txt', ['0x16f9f3000', 'monty1'])

