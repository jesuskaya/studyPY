import random

all_players = int(input('How many players: '))
mafia_cards = int(input('How many mafia: '))
peace_cards = int(input('How many peace cards: '))
doctor_cards = 1
sheriff_cards = 1
players = list(range(1, all_players + 1))


def announcement(mafias, peaces):
    print(f"Players: {all_players}")
    print(f'Number of mafia: {mafias} ')
    print(f'Number of peace cards: {peaces} ')
    print(f'Number of doctor cards: {doctor_cards}')
    print(f'Number of sheriff: {sheriff_cards} ')


def dealing_cards():
    roles = {}
    random.shuffle(players)

    mafia = random.sample(players, mafia_cards)
    for m in mafia:
        roles[m] = "Mafia"
        players.remove(m)

    peace = random.sample(players, peace_cards)
    for p in peace:
        roles[p] = "Peacefully"
        players.remove(p)

    doctor = random.choice(players)
    roles[doctor] = "Doctor"
    players.remove(doctor)

    sheriff = players[0]
    roles[sheriff] = "Sheriff"
    players.remove(sheriff)

    print("\nRoles:")
    for player, role in sorted(roles.items()):
        print(f"Player {player}: {role}")


announcement(mafias=mafia_cards, peaces=peace_cards)
dealing_cards()
