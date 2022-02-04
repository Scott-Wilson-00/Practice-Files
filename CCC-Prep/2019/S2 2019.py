import math

T = int(input())

Ns = []
for _ in range(T):
    Ns.append(int(input())*2)

def isPrime(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

pairs = []
for n in Ns:
    for i in range(2, n):
        if (isPrime(i) and isPrime(n-i)):
            pairs.append([str(i), str(n-i)])
            break

for i in range(len(pairs)):
    print(' '.join(pairs[i]))