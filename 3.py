# plan 1:
# for every sequence of numbers in the file, check if there is an adjacent  symbol
grid = []
def main():
    file = open("3.in")
    # grid of [row] [column] OR [line] [character]
    for line in file:
        grid.append(line)
    row = range(len(grid)) 
    for x in row:
        col = range(len(grid[x]))
        for y in col:
            if (grid[x][y].isnumeric()):
                check_adjacent((x, y))


def check_adjacent(point):
    x, y = point
    print(point, end=' ')
    print(grid[x][y])


main()
