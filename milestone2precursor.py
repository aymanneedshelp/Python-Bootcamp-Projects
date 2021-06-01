#global variables
import random
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    
    def __init__(self):
        self.all_cards = [] #list of all the cards
        
        for suit in suits:
            for rank in ranks:
                #creating card object
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)
    
    def shuffle(self):
        
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

class Player():
    
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == list:
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"
    
    def __len__(self):
        return len(self.all_cards)

deck = Deck()
deck.shuffle()
p1 = Player("Player 1")
p2 = Player("Player 2")

#dealing cards to player 1
for i in range(26):
    card = deck.deal_one()
    p1.add_cards(card)

#dealing cards to player 2
for i in range(26):
    card = deck.deal_one()
    p2.add_cards(card)

game_on = True
round = 0
while game_on:
    round +=1
    print(f"Round {round}")

    if len(p1) == 0:
        print("Player one out of cards! Game over!")
        print("Player two wins")
        game_on = False
        break

    if len(p2) == 0:
        print("Player two out of cards! Game over!")
        print("Player one wins!")
        game_on = False
        break

    p1_cards = []
    p1_cards.append(p1.remove_one())

    p2_cards = []
    p2_cards.append(p2.remove_one())

    at_war = True

    while at_war:
        if p1_cards[-1].value > p2_cards[-1].value:
            p1.add_cards(p1_cards)
            p1.add_cards(p2_cards)
            at_war = False

        elif p1_cards[-1].value < p2_cards[-1].value:
            p2.add_cards(p1_cards)
            p2.add_cards(p2_cards)
            at_war = False
        
        else:
            print("WAR!")
            if len(p1) < 7:
                print("Player one has insufficient cards, cannot play war")
                print("Player 2 wins!")
                game_on = False
                break
            
            elif len(p2) < 7:
                print("Player two has insufficient cards, cannot play war")
                print("Player 1 wins")
                game_on = False
                break
            else:
                for i in range(7):
                    p1_cards.append(p1.remove_one())
                    p2_cards.append(p2.remove_one())
            
