# cards.py
class Card:
    def __init__(self, rank, suit, status="in deck"):
        self.rank = rank
        self.suit = suit
        self.status = status

    def __repr__(self):
        return f"Card({self.rank}, {self.suit}, {self.status})"


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        if card not in self.cards:
            self.cards.append(card)
            return True
        return False

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        return False

    def update_card_status(self, card, new_status):
        for c in self.cards:
            if c.rank == card.rank and c.suit == card.suit:
                c.status = new_status
                return True
        return False

    def list_cards(self, status=None):
        if status:
            return [card for card in self.cards if card.status == status]
        return self.cards
