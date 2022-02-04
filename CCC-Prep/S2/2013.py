maxW = int(input())
N = int(input())

w = []
for _ in range(N):
    w.append(int(input()))

cars = 0
w4 = 0
for i in range(N):
    w4 += w[i]
    if i > 3: 
        w4 -= w[i-4]
    if w4 > maxW: 
        break
    cars += 1

print(cars)
