""" Graph the time left for both players in the same plot. """

import matplotlib.pyplot as plt
from GetTimeLeftFromPGN import getTimeLeftFromPGN


def graphTimeLeftFromPGN(pgn):
    movetimes_w, movetimes_b = getTimeLeftFromPGN(pgn)
    plt.plot(movetimes_w, label='White')
    plt.plot(movetimes_b, label='Black')
    plt.xlabel('Move')
    plt.ylabel('Time left (s)')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # read from file
    with open('pgn.txt', 'r') as file:
        pgn = file.read()
    graphTimeLeftFromPGN(pgn)
