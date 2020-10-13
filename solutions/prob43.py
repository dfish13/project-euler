from itertools import permutations

def is_substring_divisible(ls):
    if int(ls[1:4]) % 2 != 0:
        return False
    elif int(ls[2:5]) % 3 != 0:
        return False
    elif int(ls[3:6]) % 5 != 0:
        return False
    elif int(ls[4:7]) % 7 != 0:
        return False
    elif int(ls[5:8]) % 11 != 0:
        return False
    elif int(ls[6:9]) % 13 != 0:
        return False
    elif int(ls[7:]) % 17 != 0:
        return False
    return True

total = 0
for p in permutations('0123456789'):
    if is_substring_divisible(''.join(p)):
        total += int(''.join(p))
        print(''.join(p))

print(total)
