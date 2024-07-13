""" Given a PGN, get the time left for each side after each move. 
    Note that the util is simple and only works with standard cutechess format PGNs.
"""

import re

ROUNDING = 2


def getTimeLeftFromPGN(pgn):
    # get time control
    time_control = re.search(r'TimeControl \"(.*)\"', pgn)
    time_control = time_control.group(1)
    base_time, increment = time_control.split('+')
    base_time = float(base_time)
    increment = float(increment)
    time_w = time_b = base_time
    
    # remove headers, any line starting and ending with square brackets
    pgn = re.sub(r'\[.*]', '', pgn)
    movetimes_w = []
    movetimes_b = []
    last = "w"
    
    for line in pgn.split('\n'):
        if line.strip() == "":
            continue
        # loop to search for comments
        while True:
            comment_match = re.search(r'{([^}]*)}', line)
            if comment_match is None:
                break
            comment = comment_match.group(1)
            
            # get the float OR int before the 's' in the comment
            match = re.search(r'(\d+(\.\d+)?)s', comment)
            if match is None:
                continue
            time = match.group(1)  # amount of time used for the move
            
            if last == "w":
                time_w = time_w - float(time) + increment
                movetimes_w.append(round(time_w, ROUNDING))
                last = "b"
            else:
                time_b = time_b - float(time) + increment
                movetimes_b.append(round(time_b, ROUNDING))
                last = "w"
            
            # remove the comment from the line
            line = line.replace(comment_match.group(0), '')
    
    return movetimes_w, movetimes_b


if __name__ == "__main__":
    # read from file
    with open('pgn.txt', 'r') as file:
        pgn = file.read()
    print(getTimeLeftFromPGN(pgn))
