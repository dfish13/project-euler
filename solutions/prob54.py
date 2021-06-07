# Poker hands
import numpy as np

def preprocess(c):
    V = {"2": 1,
        "3": 2,
        "4": 3,
        "5": 4,
        "6": 5,
        "7": 6,
        "8": 7,
        "9": 8,
        "T": 9,
        "J": 10,
        "Q": 11,
        "K": 12,
        "A": 13}
    S = {"H": 0,
        "D": 1,
        "C": 2,
        "S": 3}
    return np.asarray((V[c[0]], S[c[1]]))

def handValue(h):
    val = 0
    h = sorted(h, key=lambda x: x[0])
    # high card
    val += h[4][0] * 14

    # pair

with open('../static/poker.txt', 'r') as pokerFile:
    hands = [tuple(l.split()) for l in pokerFile]
    hands = np.asarray(hands).flatten()
    hands = np.asarray([preprocess(c) for c in hands])
    
    hands = hands.reshape((1000, 2, 5, 2))
    wins = 0
    for a, b in hands:
        if handValue(a) > handValue(b):
            wins += 1
        print(handValue(a), handValue(b))

    print(wins)



