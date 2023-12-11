def main():
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14

    file = open("2.in")
    total = 5050 
    for game in file:
        split_game = game.split(" ")
        game_id = int(split_game[1][:-1])
        pairs = game.split(" ")[2:]
        i = 0
        length = len(pairs)//2
        while (i < length): 
            amt_clr = int(pairs[0]), pairs[1].strip(',;\n')
            match amt_clr[1]:
                case "red":
                    if (amt_clr[0] > MAX_RED):
                        i += 1
                        total -= game_id
                        break
                case "green":
                    if (amt_clr[0] > MAX_GREEN):
                        i += 1
                        total -= game_id
                        break
                case "blue":
                    if (amt_clr[0] > MAX_BLUE):
                        i += 1
                        total -= game_id
                        break
            pairs = pairs[2:]
            i += 1

    print(total)

main()
