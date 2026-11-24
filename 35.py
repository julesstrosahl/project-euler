from math import sqrt


primes = set()
def is_prime(num):
    if num in primes:
        return True
    for div in range(2,int(sqrt(abs(num)))+1):
        if num % div == 0:
            return False
    primes.add(num)
    return True

ans = 0
for i in range(2,1000000):
    istr = str(i)
    valid = True
    for j in range(len(istr)):
        k = int(istr[j:]+istr[:j])
        if not is_prime(k):
            valid = False
            break
    if not valid:
        continue
    ans += 1

print(ans)