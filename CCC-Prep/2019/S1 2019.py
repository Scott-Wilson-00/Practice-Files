flips = input()
hf = flips.count('H')
vf = flips.count('V')

def flipH():
    temp = grid[0]
    grid[0] = grid[1]
    grid[1] = temp

def flipV():
    for i in range(len(grid)):
        temp = grid[i][0]
        grid[i][0] = grid[i][1]
        grid[i][1] = temp

grid = [['1', '2'], ['3', '4']]


if hf%2 != 0:
    flipH()
if vf%2 != 0:
    flipV()

for i in range(len(grid)):
    print(" ".join(grid[i]))
