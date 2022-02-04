N = int(input())
p1 = [name.lower() for name in input().split()]
p2 = [name.lower() for name in input().split()]

gb = True

for i in range(N):
    if p2[i] == p1[p2.index(p1[i])] and p1[i] != p2[i]:
        pass
    else: 
        gb = False
        break
if gb:
    print('good')
else: 
    print('bad')