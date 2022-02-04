N = int(input())

v = []

for _ in range(N):
    v.append(int(input()))

v.sort()

minN = 100000000000

for i in range(1, len(v)-1):
    nSize = ((v[i+1] + v[i])/2)-((v[i]+v[i-1])/2)
    if nSize < minN:
        minN = nSize
    
print(round(minN,1))