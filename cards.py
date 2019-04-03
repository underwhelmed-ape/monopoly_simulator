from random import shuffle

# defining chance and community chest card functionality
# maybe improve by turning each into a class


def select_chance_card(chance_cards):
    shuffle(chance_cards)
    chance_card = chance_cards.pop()
    print(chance_card)
    print(f'number of chance cards left: {len(chance_cards)}')
    
    return chance_card


def select_community_chest_card(community_cards):
    shuffle(community_cards)
    community_card = community_cards.pop()
    print(community_card)
    print(f'number of community chest cards left: {len(community_cards)}')

    return community_card