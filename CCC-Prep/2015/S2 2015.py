Nj = int(input())
Na = int(input())

j = [input().upper() for _ in range(Nj)]

r = []
for i in range(Na):
    x = input().split()
    r.append([x[0], int(x[1])])

filled = 0

def isValid(size, jSize):
    if size == "S":
        return True
    if size == jSize:
        return True
    if size == "M" and jSize == "L":
        return True
    return False

for i in range(len(r)):
    if j[r[i][1]-1] == 'T':
        continue
    if isValid(r[i][0], j[r[i][1]-1]):
        filled += 1
        j[r[i][1]-1] = 'T'

print(filled)

        
