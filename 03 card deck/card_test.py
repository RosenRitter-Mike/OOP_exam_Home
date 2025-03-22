from card import Card
from card_suit import CardSuit
from card_rank import CardRank

ace_of_spades = Card(CardSuit.SPADES, CardRank.ACE)
king_of_hearts = Card(CardSuit.HEARTS, CardRank.KING)
nine_of_clubs = Card(CardSuit.CLUBS, CardRank.NINE)
seven_of_diamonds = Card(CardSuit.DIAMONDS, CardRank.SEVEN, False)

print(f"First card: {ace_of_spades}")
print(f"Second card: {king_of_hearts}")
print(f"Third card: {nine_of_clubs}")
print(f"Fourth card: {seven_of_diamonds}")

print(ace_of_spades == ace_of_spades)
print(ace_of_spades == king_of_hearts)

print(f"{ace_of_spades} is higher than {king_of_hearts}") if ace_of_spades > king_of_hearts \
    else print(f"{ace_of_spades} is not higher than {king_of_hearts}")

print(f"{nine_of_clubs} is higher than {king_of_hearts}") if nine_of_clubs > king_of_hearts \
    else print(f"{nine_of_clubs} is not higher than {king_of_hearts}")

print(f"{ace_of_spades} is lower than {king_of_hearts}") if ace_of_spades < king_of_hearts \
    else print(f"{ace_of_spades} is not lower than {king_of_hearts}")

print(f"{nine_of_clubs} is lower than {king_of_hearts}") if nine_of_clubs < king_of_hearts \
    else print(f"{nine_of_clubs} is not lower than {king_of_hearts}")
print("\ncard1")
print(f"Before flipping: {ace_of_spades}")
ace_of_spades.flip()
print(f"After flipping: {ace_of_spades}")
print("\ncard4")
print(f"Before flipping: {seven_of_diamonds}")
seven_of_diamonds.flip()
print(f"After flipping: {seven_of_diamonds}")
