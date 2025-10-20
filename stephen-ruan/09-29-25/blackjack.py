import random

cards = {
    1: "an ace",
    2: "a 2",
    3: "a 3",
    4: "a 4",
    5: "a 5",
    6: "a 6",
    7: "a 7",
    8: "an 8",
    9: "a 9",
    10: "a 10",
    11: "a jack",
    12: "a queen",
    13: "a king"
}

money = 100

while 3 < 4:
        print("Select Difficulty: Easy, Medium, Hard, or Insane.")
        difficulty = input()
        if difficulty == "Easy" or difficulty == "easy":
            difficulty = 1
            break
        if difficulty == "Medium" or difficulty == "medium":
            difficulty = 2
            break
        if difficulty == "Hard" or difficulty == "hard":
            difficulty = 3
            break
        if difficulty == "Insane" or difficulty == "insane":
            difficulty = 67
            break
        print("Invalid syntax, try again.")

while 1 == 1:
    while 3 < 4:
        print("You currently have $" + str(money) + ".")
        print("How much money would you like to bet? Enter a number from 5 to " + str(money) + ".")
        bet = input()
        print(type(bet))
        if int(bet) < 5 or int(bet) > money:
            print("Enter a number from 5 to " + str(money) + ".")
        elif int(bet) >= 5 and int(bet) <= money:
            print("You have now bet $" + str(bet) + ".")
            break
            
    print(" ")
    human_cards = []
    bot_cards = []
    human_cards.append(random.randint(1,13))
    human_cards.append(random.randint(1,13))
    bot_cards.append(random.randint(1,13))
    bot_cards.append(random.randint(1,13))

    def get_sum(certain_cards):
        global goon
        goon = 0
        for z in range (0, len(certain_cards)):
            if certain_cards[z] < 11:
                goon += certain_cards[z]
            else:
                goon += 10
    print(" ")

    while 3 < 4:
        output = "You currently have "
        for i in range (0, len(human_cards)):
            output += cards[human_cards[i]]
            if i == len(human_cards) - 2:
                if len(human_cards) == 2:
                    output += " and "
                else:
                    output += ", and "
            elif i == len(human_cards) - 1:
                output += "."
            else:
                output += ", "
        print(output)

        get_sum(human_cards)
        if goon > 21:
            print("Your total is now " + str(goon) + ", so you have busted.")
            print("It is now the bot's turn, type anything to continue.")
            input()
            break
        else:
            print("Your total is now " + str(goon) + ".")
        
        print("The bot has " + str(cards[bot_cards[1]]) + " and another hidden card.")
        print("Would you like to stand or hit?")
        input2 = input()
        if input2 == "hit" or input2 == "Hit" or "hit" in input2 or "Hit" in input2:
            if difficulty == 1:
                if random.randint(1,3) < 3 and goon > 15:
                    human_cards.append(random.randint(1,5))
                elif random.randint(1,3) < 3 and goon > 11 and goon < 16:
                    human_cards.append(random.randint(1,9))
                else:
                    human_cards.append(random.randint(1,13))
            elif difficulty == 2:
                human_cards.append(random.randint(1,13))
            else:
                if random.randint(1,9) < 4 + (difficulty == 67) * 4 and goon > 15:
                    human_cards.append(random.randint(6,13))
                elif random.randint(1,9) < 4 + (difficulty == 67) * 4 and goon > 11 and goon < 16:
                    human_cards.append(random.randint(10,13))
                else:
                    human_cards.append(random.randint(1,13))
            print(" ")
            print("Your new card is " + str(cards[human_cards[-1]]) + ".")
        else:
            input("You have decided to stand, so it's now the bot's turn. Type anything to continue")
            break

    human_sum = goon
    print(" ")
    while 3 < 4:
        output = "The bot's cards are currently "
        for i in range (0, len(bot_cards)):
            output += cards[bot_cards[i]]
            if i == len(bot_cards) - 2:
                if len(bot_cards) == 2:
                    output += " and "
                else:
                    output += ", and "
            elif i == len(bot_cards) - 1:
                output += "."
            else:
                output += ", "
        print(output)
        get_sum(bot_cards)
        if goon > 21:
            print("The bot's total is now " + str(goon) + ", so the bot busted.")
            break
        else:
            print("The bot's total is now " + str(goon) + ".")
        print("Type anything to continue.")
        input()

        if difficulty == 67 and goon > human_sum:
            print("The bot decides to stand.")
            break
        elif goon <= 16:
            if difficulty == 67 and random.randint(1,6) == 1:
                bot_cards.append(21 - goon)
            elif difficulty == 67 and random.randint(1,4) == 1:
                bot_cards.append(random.randint(goon+1,21) - goon)
            else:
                bot_cards.append(random.randint(1,13))
            print("The bot decides to hit and draws a " + str(cards[bot_cards[-1]]) + ".")
        elif difficulty == 67 and goon <= 19:
            bot_cards.append(random.randint(goon+1,22) - goon)
        else:
            print("The bot decides to stand.")
            break

    print("Type anything to reveal the final results")
    input()
    bot_sum = goon

    print("You have a total of " + str(human_sum) + " and the bot has a total of " + str(bot_sum) + ".")
    if bot_sum > 21 and human_sum > 21:
        print("Both you and the bot busted.")
        if human_sum > bot_sum:
            print("Since you have a bigger bust, you lose.")
            money -= int(bet)
        elif human_sum == bot_sum:
            print("Both players have the same score, so you tie.")
        else:
            print("Since the bot has a bigger bust, you win!")
            money += int(bet)
    elif bot_sum > 21 and human_sum <= 21:
        print("The bot busted, but you didn't, so you win!")
        money += int(bet)
    elif bot_sum <= 21 and human_sum > 21:
        print("You busted, but the bot didn't, so you lose.")
        money -= int(bet)
    else:
        if bot_sum > human_sum:
            print("The bot has a higher score, so you lose.")
            money -= int(bet)
        elif bot_sum == human_sum:
            print("Both players have the same score, so you tie.")
        else:
            print("You have a higher score, so you win!")
            money += int(bet)
        print("You currently have " + str(money) + ".")
    if money < 5:
        print("You don't have enough money to play again :(")
        break
    else:
        print(" ")
        continue

    