import math

N = int(input())
m = [int(x) for x in input().split()]

m.sort()

if len(m)%2 == 0:
    x = 0
else:
    x = 1

l = m[:int(math.floor(len(m)/2)) + x]
h = m[int(math.floor(len(m)/2)) + x:]

l.reverse()

for i in range(len(h)):
    print(l[i], end=" ")
    print(h[i], end=" ")

if x == 1:
    print(l[-1])
