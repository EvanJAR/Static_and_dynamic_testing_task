import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_game = CardGame()

        self.card1 = Card("Clubs", 1)
        self.card2 = Card("Hearts", 10)
        self.card3 = Card("Hearts", 9)
        self.card4 = Card("Diamonds", 8)

        self.cards = [self.card1, self.card2, self.card3, self.card4]


    def test_check_for_ace_true(self):
        self.assertTrue(self.card_game.check_for_ace(self.card1))
    
    def test_check_for_ace_false(self):
        self.assertFalse(self.card_game.check_for_ace(self.card2))
    
    def test_highest_card_card1(self):
        self.assertEqual(self.card2, self.card_game.highest_card(self.card2, self.card4))

    
    def test_highest_card_card2(self):
        self.assertEqual(self.card2, self.card_game.highest_card(self.card4, self.card2))
    
    def test_cards_total(self):
        self.assertEqual("You have a total of 28", self.card_game.cards_total(self.cards))