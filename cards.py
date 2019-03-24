from random import shuffle

# defining chance and community chest card functionality
# maybe improve by turning each into a class


def select_chance_card():
    chance_cards = ['Drunk', 0, 39, 24, 13,
    'bank_pays', 'gooj', 'back_3', 10, 'house_repairs', 
    'fees', 'fine', 5, 'street_repairs', 'crossword', 'loan']
    
    shuffle(chance_cards)
    chance_card = chance_cards.pop()
    print(chance_card)
    
    return chance_card


def select_community_chest_card():
    community_cards = [0, 19, 10, 'hospital', 'doctors', 'insurance', 'ban_error', 
    'annuity', 'inherit', 'stock', 'interest', 'refund', 'prize', 'birthday', 'gooj', 'pay'] 

    shuffle(community_cards)
    community_card = community_cards.pop()
    print(community_card)

    return community_card

select_chance_card()
