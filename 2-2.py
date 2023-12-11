def main():
    file = open("2.in")
    powers = 0
    for game in file:
        print(game)
        split_game = game.split(":")
        game_id = int(split_game[0][5:])
        print("GAME ID: ", game_id)
        rounds = split_game[1].split(';')
        print("ROUNDS: ", rounds)
        highest_red = 0
        highest_blue = 0
        highest_green = 0
        for round in rounds:
            pairs = round.strip(" ").split(" ")
            i = 0
            length = len(pairs)//2
            while (i < length): 
                amt_clr = int(pairs[0]), pairs[1].strip(' ,;\n')
                match amt_clr[1]:
                    case "red":
                        if (amt_clr[0] > highest_red):
                            highest_red = amt_clr[0]
                        i += 1
                    case "green":
                        if (amt_clr[0] > highest_green):
                            highest_green = amt_clr[0]
                        i += 1
                    case "blue":
                        if (amt_clr[0] > highest_blue):
                            highest_blue = amt_clr[0]
                        i += 1
                pairs = pairs[2:]
        print("HIGHEST RED: ", highest_red)
        print("HIHGEST GREEN: ", highest_green)
        print("HIGHEST BLUE: ", highest_blue)
        power = highest_red * highest_blue * highest_green
        powers += power

    print(powers)
main()
