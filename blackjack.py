import random
values = {"King":10,"Queen":10,"Jack":10,"Ace":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,
          "Eight":8,"Nine":9,"Ten":10}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card():
    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    def __init__(self):
        self.all_cards = []
        for rank in ranks:
            for suit in suits:
                new_card = Card(rank,suit)
                self.all_cards.append(new_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal(self):
        return self.all_cards.pop()

class Player():
    def __init__(self,name,bank):
        self.name = name
        self.bank = bank
        self.hand = []
        
    def hit(self,card):
        self.hand.append(card)

class Dealer():
    def __init__(self):
        self.hand = []
    
    def hit(self,card):
        self.hand.append(card)

player_name = input("Enter the Player name: ")
player_bank = int(input(f"Enter {player_name}'s bankroll: "))
print()

play = True
while play == True:

    player = Player(player_name,player_bank)
    dealer = Dealer()

    deck = Deck()
    deck.shuffle()

    #checking bet
    while True:
        bet = int(input(f"{player.name} enter your bet amount: "))
        if bet > player.bank:
            print("Insufficient funds, place a different bet")
        elif player.bank == 0:
            print(f"{player.name} has no money left, cannot play")
            game_on = False
            player_turn = False
            player_lose = True
        else:
            break

    #game start / inititialize

    for i in range(2):
        player.hit(deck.deal())
        dealer.hit(deck.deal())

    def check_ace():
        for card in player.hand:
            if card.rank == "Ace":
                choice = int(input("Would you like your Ace to be 1 or 11: "))
                card.value = choice
                card.rank = "Ace "

    def calc_sum():
        check_ace()
        s = 0
        for card in player.hand:
            s += card.value
        return s

    print(f"{player.name}'s cards are:")
    for card in player.hand:
        print(card,end=", ")
    print()
    print()

    s1=calc_sum()
    print(f"{player.name}'s sum is: {s1}")
    print()

    print(f"Dealer's card is: {dealer.hand[0]}")
    print()

    player_sum = 0
    dealer_sum = 0


    game_on = True
    player_turn = True
    player_lose = False

    def check_bust(sum):
        if sum > 21:
            player_lose = True
            print(f"BUST! {player.name}'s hand is worth {sum}")
            print()
            player_turn = False
            game_on = False
            return True
        else:
            print(f"{player.name}'s total is {sum}")
            print()
            return False

    while game_on:

        #starting game       
        while player_turn:
            choice = input("Hit(H) or Stay(S): ")

            if choice.upper() == "H":
                player.hit(deck.deal())
                print(f"{player.name}'s cards are:")
                for card in player.hand:
                    print(card,end=", ")
                print()
                sum = calc_sum()
                bust = check_bust(sum)
                if bust == True:
                    player_turn = False
                    player_lose = True
            
            elif choice.upper() == "S":
                print(f"{player.name}'s cards are:")
                for card in player.hand:
                    print(card,end=", ")
                print('\n')
                print()
                sum = calc_sum()
                check_bust(sum)
                player_turn = False
            
            else:
                print("Wrong input, try again!")
                print()

        if player_lose == True:
            print()
            print(f"DEALER WINS! {player.name} loses their bet")
            player.bank -= bet
            break
        else:
            dealer_sum = 0
            for card in dealer.hand:
                dealer_sum += card.value

            if dealer_sum <= 21 and dealer_sum <= sum:
                dealer.hit(deck.deal())
                print()
                print("DEALER HIT!")
                print()
                print(f"Dealer's cards are:")
                for card in player.hand:
                    print(card,end=", ")
                print()
                print()
            elif dealer_sum <=21 and dealer_sum > sum:
                print()
                print(f"Dealer's cards are:")
                for card in player.hand:
                    print(card,end=", ")
                print()
                print()
                print(f"Dealer has a score of {dealer_sum} which is closer to 21 than {sum}")
                print(f"DEALER WINS! {player.name} loses their bet")
                player.bank -= bet
                game_on = False
            elif dealer_sum > 21:
                print()
                print(f"Dealer's cards are:")
                for card in player.hand:
                    print(card,end=", ")
                print()
                print(f"DEALER HAS BUST! {player.name} wins!")
                print()
                player.bank += bet
                game_on = False

    player_bank = player.bank
    print(f"{player.name} has {player.bank}")
    print()
    ask = input("Would you like to play again?(Y/N) ")
    if ask.upper() == 'N':
        play = False
