# Poker hands


with open('poker.txt', 'r') as pokerFile:
    hands = [tuple(l.split()) for l in pokerFile]

    print(hands[:5])
