
total = 0
s = set()
for i in range(1, 20):
    for j in range(1, 30):
        if len(str(i**j)) == j:
            total += 1
            s.add(i**j)
            print('{}**{} = {}'.format(i, j, i**j))
print(total)
print(len(s))
