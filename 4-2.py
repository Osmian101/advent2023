# traverse backward through the won scratch cards, 

def main():
    ans = 0
    totals = {}
    queue = []
    file = open("4.in")
    for line in file:
        i = 0
        game_id = line.split("|")[0].split(":")[0]
        # print("Card{:>4}".format("1"))
        winning_numbers = line.split("|")[0].split(":")[1]
        winning_numbers = [x for x in winning_numbers.strip().split(' ') if x != ''] 
        played_numbers = [x for x in line.split("|")[1].strip().split(' ') if x != '']
        for number in winning_numbers:
            if (number in played_numbers):
                i += 1
                continue
        totals.update({game_id: [i]})
    
    print(totals)
    card_id = 1
    while (totals):
        bonus_cards = totals.pop("Card{:>4}".format(str(card_id)))
        print(bonus_cards)
        add_cards_to = range(1, bonus_cards[0] + 1)
        for x in add_cards_to:
            totals["Card{:>4}".format(str(card_id + x))].append(bonus_cards[0])
        while (bonus_cards):
            #print(bonus_cards.pop(0))
            ans += bonus_cards.pop(0)
            #print(ans)
        card_id += 1
    # go through each card one at a time, 
    # new card -> add each bonus card to the queue, i + 1
    print(ans)

main()
