#Draw a card project
import random

def create_deck(): #function to reuse the deck
    suits = ["♥", "♦", "♣", "♠"] #4 suits
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] #13 ranks
    deck = [(suit, rank) for suit in suits for rank in ranks] #card creation
    random.shuffle(deck)
    return deck

def draw_card(deck, number_cards): #function to draw n cards from the deck
    hand = deck[:number_cards]
    del deck[:number_cards]
    return hand, deck

deck = create_deck()

def show_card(card): #draws cards one by one
    space = " "
    if len(card[1]) == 2:
        space = ""
    print (f"""
    +---------+
    |{card[1]}       {space}|
    |         |
    |    {card[0]}    |
    |         |
    |{space}       {card[1]}|
    +---------+
    """)  

while len(deck) > 0: #loop to draw cards until deck is empty
    num_cards = int(input("How many cards do you want to draw? ")) #user decides how many cards to draw
    hand, deck = draw_card(deck,num_cards)
    for card in hand:
        show_card(card)

print("We are out of cards")
