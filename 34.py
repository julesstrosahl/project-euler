from math import factorial

ans = 0
maxless = 0
maxhigh = 0
maxright = 0
for i in range(10,100000):
    fsum = sum(factorial(int(j)) for j in str(i))
    if fsum != i:
        if fsum < i:
            maxless = i
        elif fsum > i:
            maxhigh = i
        continue
    maxright = i
    ans += i

print(ans)