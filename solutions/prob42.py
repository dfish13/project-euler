import math


with open('../files/p042_words.txt', 'r') as wordsFile:
    words = [w[1:-1] for w in wordsFile.read().split(',')]

triangleNums = set()
maxWordScore = 0
wordScoreDict = dict()
for w in words:
     wordScore = sum(ord(c) - ord('A') + 1 for c in w)
     wordScoreDict[wordScore] = wordScoreDict.get(wordScore, 0) + 1
     if wordScore > maxWordScore:
         maxWordScore = wordScore

n = math.floor((2*maxWordScore)**0.5) + 1

for i in range(1, n):
    triangleNums.add(i*(i + 1)/2)

total = 0
for k, v in wordScoreDict.items():
    if k in triangleNums:
        total += v

print(total)
