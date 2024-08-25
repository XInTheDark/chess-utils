""" Graph the time used for both players in the same plot. """

import matplotlib.pyplot as plt
from GetTimeUsedFromPGN_depr import getTimeUsedFromPGN

def graphTimeLeftFromPGN(pgn):
    movetimes_w, movetimes_b = getTimeUsedFromPGN(pgn)
    plt.plot(movetimes_w, label='White')
    plt.plot(movetimes_b, label='Black')
    plt.xlabel('Move')
    plt.ylabel('Time used (s)')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # read from file
    with open('pgn.txt', 'r') as file:
        pgn = file.read()
    graphTimeLeftFromPGN(pgn)
