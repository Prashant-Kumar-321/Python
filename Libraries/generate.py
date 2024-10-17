import random 

coin = random.choice(['Head', 'Tail'])
number = random.randint(1, 6)

cards = ["Jack", "Queen", "King"]
random.shuffle(cards)

# print(f"Coint {coin}")
# print(f"Random Number {number}")

for card in cards: 
    print(card)