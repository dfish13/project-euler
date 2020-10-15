

G = set()

with open('p079_keylog.txt', 'r') as keylogFile:
	for l in keylogFile:
		code = l.strip()
		G.add((code[0], code[1]))
		G.add((code[0], code[2]))
		G.add((code[1], code[2]))

print(G)
		
