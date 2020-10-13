

with open('../files/p022_names.txt', 'r') as namesFile:
    names = [name[1:-1] for name in namesFile.read().split(',')]
    names.sort()

    total = 0

    for i, n in enumerate(names):
        namescore = sum(ord(c)-ord('A')+1 for c in n)
        total += (i+1)*namescore

    print(total)
