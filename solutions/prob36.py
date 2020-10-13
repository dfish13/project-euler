
def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s) - (i + 1)]:
            return False
    return True

total = 0
for n in range(1, 1000000):
    if is_palindrome(str(n)) and is_palindrome(bin(n)[2:]):
        print(n, bin(n)[2:])
        total += n
print(total)
