def main():
    totals = []
    file = open("4.in")
    for line in file:
        i = 0
        winning_numbers = line.split("|")[0].split(":")[1]
        winning_numbers = [x for x in winning_numbers.strip().split(' ') if x != ''] 
        print(winning_numbers)
        played_numbers = [x for x in line.split("|")[1].strip().split(' ') if x != '']
        print(played_numbers)
        for number in winning_numbers:
            if (number in played_numbers):
                i += 1
                continue
        totals.append(i)
    print(totals)
    total = 0
    for num in totals:
        if (num == 0):
            total += 0
        elif (num == 1):
            total += 1
        elif (num == 2):
            total += 2
        elif (num == 3):
            total += 4
        elif (num == 4):
            total += 8
        elif (num == 5):
            total += 16
        elif (num == 6):
            total += 32
        elif (num == 7):
            total += 64
        elif (num == 8):
            total += 128
        elif (num == 9):
            total += 256
        elif (num == 10):
            total += 512

    print(total)

main()
