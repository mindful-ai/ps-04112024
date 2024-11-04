# test_cards.py
import pytest
from cards import Card, Deck

def test_add_card():
    deck = Deck()
    card = Card("A", "Hearts")
    assert deck.add_card(card) == True
    assert len(deck.cards) == 1
    assert deck.cards[0] == card

def test_prevent_duplicate_addition():
    deck = Deck()
    card = Card("A", "Hearts")
    deck.add_card(card)
    assert deck.add_card(card) == False
    assert len(deck.cards) == 1  # Only one instance should be present

def test_remove_card():
    deck = Deck()
    card = Card("A", "Hearts")
    deck.add_card(card)
    assert deck.remove_card(card) == True
    assert len(deck.cards) == 0

def test_remove_nonexistent_card():
    deck = Deck()
    card = Card("A", "Hearts")
    assert deck.remove_card(card) == False  # Card is not in the deck

def test_update_card_status():
    deck = Deck()
    card = Card("A", "Hearts")
    deck.add_card(card)
    assert deck.update_card_status(card, "discarded") == True
    assert card.status == "discarded"

def test_list_cards_no_filter():
    deck = Deck()
    deck.add_card(Card("A", "Hearts"))
    deck.add_card(Card("K", "Spades"))
    assert len(deck.list_cards()) == 2

def test_list_cards_with_filter():
    deck = Deck()
    card1 = Card("A", "Hearts", status="in deck")
    card2 = Card("K", "Spades", status="discarded")
    deck.add_card(card1)
    deck.add_card(card2)
    in_deck_cards = deck.list_cards(status="in deck")
    discarded_cards = deck.list_cards(status="discarded")

    assert len(in_deck_cards) == 1
    assert in_deck_cards[0] == card1
    assert len(discarded_cards) == 1
    assert discarded_cards[0] == card2
