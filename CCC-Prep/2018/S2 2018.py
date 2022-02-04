N = int(input())

g = []
for _ in range(N):
    g.append([int(f) for f in input().split()])

def print_grid(grid):
    for i in range(N):
        for j in range(N):
            grid[i][j] = str(grid[i][j])
        print(" ".join(grid[i]))

def rot(g):
    ng = []
    for i in range(N-1, -1, -1):
        ng.append([g[j][i] for j in range(N)])
    return ng

if g[0][0] < g[0][1] and g[0][0] < g[1][0]:
    print_grid(g)

elif g[0][0] > g[0][1] and g[0][0] < g[1][0]:
    print_grid(rot(g))

elif g[0][0] > g[0][1] and g[0][0] > g[1][0]:
    print_grid(rot(rot(g)))

elif g[0][0] < g[0][1] and g[0][0] > g[1][0]:
    print_grid(rot(rot(rot(g))))