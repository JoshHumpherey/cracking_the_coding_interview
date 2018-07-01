# Cracking the Coding Interview: 7.1
# Written by Josh Humphrey

class deck():

    def __init__(self):
        self.available = []

    def populate_deck(self):
        suits = ["Diamonds", "Hearts", "Spades","Clubs"]
        values = ["1","2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
        for suit in suits:
            for val in values:
                if suit == "Hearts" or suit == "Diamonds":
                    temp_card = self.card(suit,val,"Red")
                else:
                    temp_card = self.card(suit,val,"Black")
                self.available.append(temp_card)

    def print_remaining(self):
        for card in self.available:
            suit = card.suit
            val = card.value
            color = card.color
            print("Card[" + str(suit) + ", " + str(val) + ", " + str(color) + "]")

    class card():

        def __init__(self, suit, value, color):
            self.suit = suit
            self.value = value
            self.color = color


card_deck = deck()
card_deck.populate_deck()
card_deck.print_remaining()
