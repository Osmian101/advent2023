# plan 1:
# for every sequence of numbers in the file, check if there is an adjacent  symbol
# index every number sequence in the file for later reference, as a range of points

# plan 2:
# for every symbol check adjacent spaces for a number, reference that point in the 
# number list to get the rest of the sequence. 

grid = []
numbers = []
symbols = []
valids = set()
adjacent_eight = [(-1, -1), (-1, 0), (-1, 1), 
                 (0, -1),           (0, 1),
                 (1, -1), (1, 0), (1, 1)]

def main():
    file = open("3.in")
    # grid of [row] [column] OR [line] [character]
    for line in file:
        grid.append(line)
    # TODO: fix off by one / boundary detection
    row = range(len(grid) - 1) 
    for x in row:
        col = range(len(grid[x]) - 1)
        for y in col:
            if (grid[x][y].isnumeric()):
                numbers.append((x, y))
            elif (not grid[x][y].isnumeric() and grid[x][y] !=  '.'):
                symbols.append((x, y))
                check_adjacent((x, y))
                # if one of the adjacent points is a number
                # find it in the numbers list, and get its immediate neighbors
    print(valids)
    ans = 0
    for num in valids:
        ans += int(num)
    print(ans)


def check_adjacent(base):
    for point in adjacent_eight:
        x_a, y_a = add_points(base, point)
        if (grid[x_a][y_a] is not None):
            if (grid[x_a][y_a].isnumeric()):
                get_number_string((x_a, y_a))
                # print(grid[base[0]][base[1]], " ", (x_a,y_a), ": ", grid[x_a][y_a])


def get_number_string(point):
    x, y = point
    valid = str(grid[x][y])
    valid = populate_left_of(point, valid)     
    valid = populate_right_of(point, valid)
    valids.add(valid)


def populate_left_of(point, string):
    x, y = point
    i = 1
    while (grid[x][y - i].isnumeric()):
        string = str(grid[x][y - i]) + string    
        i += 1
    return string

def populate_right_of(point, string):
    x, y = point
    i = 1
    while (grid[x][y + i].isnumeric()):
        string = string + str(grid[x][y + i])
        i += 1
    return string

def add_points(point_1, point_2):
    return (point_1[0] + point_2[0], point_1[1] + point_2[1])


main()
