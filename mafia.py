import random

all_players = int(input('How many players: '))
mafia_cards = int(input("Enter mafia number of players: "))
peace_cards = int(input("Enter peace number of players: "))
doctor_cards = 1
sheriff_cards = 1
players = list(range(1, all_players + 1))


def mafia_play(mafias, peaces):
    print(f"Mafia cards will be {mafias} and peace cards will be {peaces}")
    print(f"Doctor cards will be {doctor_cards}")
    print(f"Sheriff cards will be {sheriff_cards}")


def dealing_cards():
    random.shuffle(players)
    roles = {}

    mafia = random.sample(players, mafia_cards)
    for m in mafia:
        roles[m] = "Мафия"
        players.remove(m)

    peaceful = random.sample(players, peace_cards)
    for p in peaceful:
        roles[p] = "Мирный"
        players.remove(p)

    doctor = random.choice(players)
    roles[doctor] = "Доктор"
    players.remove(doctor)

    sheriff = players[0]
    roles[sheriff] = "Шериф"

    print("\nRoles:")
    for player, role in sorted(roles.items()):
        print(f"Player {player}: {role}")


mafia_play(mafias=mafia_cards, peaces=peace_cards)
dealing_cards()
