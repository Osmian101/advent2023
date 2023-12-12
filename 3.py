# plan 1:
# for every sequence of numbers in the file, check if there is an adjacent  symbol
# index every number sequence in the file for later reference, as a range of points
grid = []
adjacent_eight = [(-1, -1), (-1, 0), (-1, 1), 
                 (0, -1),           (0, 1),
                 (1, -1), (1, 0), (1, -1)]

def main():
    file = open("3.in")
    # grid of [row] [column] OR [line] [character]
    for line in file:
        grid.append(line)
    row = range(len(grid) - 1) 
    for x in row:
        col = range(len(grid[x]) - 1)
        for y in col:
            if (grid[x][y].isnumeric()):
                check_adjacent((x, y))


def check_adjacent(base):
    for point in adjacent_eight:
        x_a, y_a = add_points(base, point)
        if (grid[x_a][y_a] is not None):
            if (not grid[x_a][y_a].isnumeric() and grid[x_a][y_a] is not '.'):
                print(grid[base[0]][base[1]], " ", (x_a,y_a), ": ", grid[x_a][y_a])
#           print(grid[x_a][y_a], end=' ')

    #print(point, end=' ')
    #print(grid[x][y])


def add_points(point_1, point_2):
    return (point_1[0] + point_2[0], point_1[1] + point_2[1])


main()
