from itertools import combinations_with_replacement



key_len = 3

with open('p059_cipher.txt', 'r') as cipherFile:
    asciiVals = [int(x) for x in cipherFile.read().split(',')]

    L = []
    for i in range(key_len):
        offset = 0
        d = dict()
        while i + offset < len(asciiVals):
            d[asciiVals[i + offset]] = d.get(asciiVals[i + offset], 0) + 1
            offset += key_len
        ms = sorted(d.items(), key=lambda x: x[1], reverse=True)
        L.append([x[0] ^ ord(' ') for x in ms])

    for c in combinations_with_replacement(list(range(1)), 3):
        key = (L[0][c[0]], L[1][c[1]], L[2][c[2]])
        newVals = []
        i = 0
        while i < len(asciiVals):
            newVals.append(asciiVals[i] ^ key[i % key_len])
            i += 1
        print(key)
        print(''.join(chr(x) for x in newVals))
        print(sum(newVals))

    
