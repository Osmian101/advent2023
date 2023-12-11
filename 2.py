def main():

    max = {"red":12, "green":13, "blue":14}

    file = open("2.in")
    total = 0
    for game in file:
        print(game)
        split_game = game.split(" ")
        game_id = split_game[1][:-1]
        print("GAME ID: " + game_id)
        pairs = game.split(" ")[2:]
        amt_clr = pairs[0], pairs[1].strip(',')
        print(amt_clr)
        match amt_clr[1]:
            case "red":
                total += int(amt_clr[0]) if int(amt_clr[0]) < max["red"] else 0
            case "green":
                total += int(amt_clr[0]) if int(amt_clr[0]) < max["green"] else 0
            case "blue":
                total += int(amt_clr[0]) if int(amt_clr[0]) < max["blue"] else 0
    print(total)


main()
