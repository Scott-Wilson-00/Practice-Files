T = int(input())
tests = []
for _ in range(T):
    N = int(input())
    test = []
    for _ in range(N):
        test.append(int(input()))
    tests.append(test)

def solve(carts):
    ans = carts.copy()
    ans.sort()
    branch = [1000000]
    lake = [0]
    while len(carts) > 0:
        # if next cart should go in lake
        if carts[-1] == lake[-1] + 1:
            x = carts.pop()
            lake.append(x)
        
        # if next branch cart shouldn't go in lake
        elif branch[-1] != lake[-1] + 1:

            #if next cart can go on branch
            if carts[-1] < branch[-1]:
                x = carts.pop()
                branch.append(x)
            else:
                print('N')
                return None
        
        # if next branch cart should go in lake
        else:
            x = branch.pop()
            lake.append(x)

    # if all carts got to lake
    print('Y')


for i in range(len(tests)):
    solve(tests[i])


