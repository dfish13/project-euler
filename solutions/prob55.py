

def isPalindrome(n):
    sn = str(n)
    for i in range(len(sn)//2):
        if sn[i] != sn[-(i + 1)]:
            return False
    return True


def lychrel(n):
    return n + int(str(n)[::-1])

total = 0

for i in range(10000):
    n = lychrel(i)
    for j in range(48):
        if isPalindrome(n):
            break
        n = lychrel(n)
        if j == 47:
            total += 1
    
print(total)
