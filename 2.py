def main():

    max = {"red":12, "green":13, "blue":14}

    file = open("2.in")
    for game in file:
        print(game)
        split_game = game.split(" ")
        game_id = split_game[1][:-1]
        print(game_id)
        for eme in game.split(" ")[2:]:
            print(eme)
main()
