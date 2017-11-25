import random

class PlayingCard(object):
    """Playing card to be used to fill a baccarat shoe and
    to be drawn to a playing hand.

    Attributes:
        rank: int or a string with the rank of the card.
        suit: string with the suit of the card
    """
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def value(self):
        """Returns the value of the card according to 
        baccarat rules.
        """
        if self.rank in range(2, 10):
            return self.rank
        elif self.rank == 'ace':
            return 1
        else:
            return 0

    def __add__(self, other):
        return (self.value + other) % 10

    __radd__ = __add__

    def __repr__(self):
        """Return the representation string as if the object was
        called when creating a new instance.
        """
        return f'PlayingCard({self.rank}, \'{self.suit}\')'

    def __str__(self):
        """Return a string with the rank and suit of the card.
        """
        return '{} of {}'.format(self.rank, self.suit)

class Shoe(object):
    def __init__(self, num_decks):
        self.num_decks = num_decks
        self.add_decks()

    def add_decks(self):
        suits = ['hearts', 'spades', 'clubs', 'diamonds']
        ranks = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
        self.cards = []
        for i in range(self.num_decks):
            for suit in suits:
                for rank in ranks:
                   self.cards.append(PlayingCard(rank, suit)) 
        random.shuffle(self.cards)

    def __repr__(self):
        """Return the representation string as if the object was
        called when creating a new instance.
        """
        return f'Shoe({self.num_decks})'

    def __str__(self):
        return '{} decks shoe. {} cards left.\n'.format(self.num_decks, len(self.cards)) + \
               ', '.join([card.__str__() for card in self.cards])
               
