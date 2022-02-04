N = int(input())
swif = [int(x) for x in input().split()]
sea = [int(x) for x in input().split()]

sumSwif = 0
sumSea = 0

K = 0

for i in range(N):
    sumSwif += swif[i]
    sumSea += sea[i]
    if sumSea == sumSwif:
        K = i+1

print(K)
