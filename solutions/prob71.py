import math

closest = (2, 5)
f = 3 / 7
smallestDif = f - (closest[0] / closest[1])
for d in range(8, 1000001):
  a, b = (math.floor(f * d), d)
  if math.gcd(a, b) > 1:
    continue
  dif = f - (math.floor(f * d) / d)
  if dif < smallestDif:
    smallestDif = dif
    closest = (math.floor(f * d), d)

print(closest)