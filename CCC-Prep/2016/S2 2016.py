c = int(input())
N = int(input())
dmo = [int(x) for x in input().split()]
peg = [int(x) for x in input().split()]

dmo.sort()
peg.sort()

pairs = []

if c == 1:
    tspeed = 0
    for i in range(N):
        pairs.append([dmo[i], peg[i]])
    tspeed = sum([max(pairs[i]) for i in range(N)])
    print(tspeed)

if c == 2:
    peg.reverse()
    tspeed = 0
    for i in range(N):
        pairs.append([dmo[i], peg[i]])
    tspeed = sum([max(pairs[i]) for i in range(N)])
    print(tspeed)