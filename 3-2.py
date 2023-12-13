# idea 1: create a dict of valids with the symbol and point they were put in with, 
# if the symbol is a gear and the point is the same then multiply them
previous_valid = ""
previous_gear = ((0,0),'*')
grid = []
numbers = []
symbols = []
valids = [] 
gears = []
adjacent_eight = [(-1, -1), (-1, 0), (-1, 1), 
                 (0, -1),           (0, 1),
                 (1, -1), (1, 0), (1, 1)]

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
                numbers.append((x, y))
            elif (not grid[x][y].isnumeric() and grid[x][y] !=  '.'):
                symbols.append((x, y))
                check_adjacent((x, y))
                # if one of the adjacent points is a number
    
    ans = 0
    for num in valids:
        ans += int(num)
    print(ans)
    ans2 = 0
    for num in gears:
        ans2 += num
    print(ans2)

def check_adjacent(base):
    for point in adjacent_eight:
        x_a, y_a = add_points(base, point)
        if (grid[x_a][y_a] is not None):
            if (grid[x_a][y_a].isnumeric()):
                get_number_string((x_a, y_a), base)


def get_number_string(point, base):
    global previous_valid
    global previous_gear
    x, y = point
    gear = (base, grid[base[0]][base[1]])
    valid = str(grid[x][y])
    valid = populate_left_of(point, valid)     
    valid = populate_right_of(point, valid)
    if (valid != previous_valid):
        valids.append(valid)
        if (gear == previous_gear):
            gears.append(int(valid)*int(previous_valid))
    previous_valid = valid
    previous_gear = gear


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
