from functools import reduce
from operator import mul


ans = []
for i in range(10,100):
    for j in range(i+1,100):
        ij = i/j
        istr = str(i)
        jstr = str(j)
        iset = set(istr)
        jset = set(jstr)
        inter = iset.intersection(jset)
        for x in inter:
            iixs = [i for i,y in enumerate(istr) if y==x]
            jixs = [i for i,y in enumerate(jstr) if y==x]
            inums = [int(istr[0:i]+istr[i+1:]) for i in iixs]
            jnums = [int(jstr[0:i]+jstr[i+1:]) for i in jixs]
            for ni in inums:
                for nj in jnums:
                    if (ni == i/10 and nj == j/10) or nj == 0:
                        continue
                    if ni/nj != ij:
                        continue
                    ans.append([i,j,ni,nj])

num = reduce(mul, (ni for [i,j,ni,nj] in ans), 1)
den = reduce(mul, (nj for [i,j,ni,nj] in ans), 1)

print(den/num)