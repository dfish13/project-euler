# Odd period square roots

import math
import sympy
N = 23



def conFrac(n):
    ip = math.floor(n ** 0.5)
    if ip * ip == n:
        return 0
    num = 1
    den = ip
    i = 0
    while 1:
        top = den + ip
        bot = (n - den * den) // num
        y = top // bot
        i += 1
        num = bot
        den = - (den - bot * y)
        if num == 1 and den == ip:
            return i

print(sum(conFrac(i) % 2 for i in range(2, 10001)))
