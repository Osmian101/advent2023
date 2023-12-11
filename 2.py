def main():
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14

    file = open("2.in")
    total = 5050 
    for game in file:
        split_game = game.split(" ")
        game_id = int(split_game[1][:-1])
        print("GAME ID: ", game_id)
        pairs = game.split(" ")[2:]
        print(pairs)
        i = 0
        length = len(pairs)//2
        # print("TOTAL: ", total)
        while (i < length): 
            amt_clr = pairs[0], pairs[1].strip(',;\n')
            print(amt_clr)
            match amt_clr[1]:
                case "red":
                    if (int(amt_clr[0]) > MAX_RED):
                        i += 1
                        total -= game_id
                        break
                case "green":
                    if (int(amt_clr[0]) > MAX_GREEN):
                        i += 1
                        total -= game_id
                        break
                case "blue":
                    if (int(amt_clr[0]) > MAX_BLUE):
                        i += 1
                        total -= game_id
                        break
            pairs = pairs[2:]
            i += 1

    print(total)

main()
