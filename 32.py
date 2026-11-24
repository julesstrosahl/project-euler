ans = set()
for i in range(1,10000):
    for j in range(i,10000):
        p = i*j
        if p in ans:
            continue
        s = str(i)+str(j)+str(p)
        if len(s) > 9:
            break
        if len(s) < 9:
            continue
        if not all(str(k) in s for k in range(1,10)):
            continue
        ans.add(p)
        print(f"{i}*{j}={p}")

print(sum(ans))