import random

def roll_dice():
    return random.randint(1, 6)

def elemental_dice():
    elements = ['Fire', 'Earth', 'Water', 'Air']
    random_index = random.randint(0, len(elements) - 1)
    random_element = elements[random_index]
    return random_index, random_element

    # TEXT BASED GAME

# The first dice has 6 sides
# The second dice has 4 sides that are linked to 4 elemets
# If you roll a 6 then you cancel out the opponents resestence

def attack(attacker, defender):

    if attacker['name'] == 'Player':
        attacker_color = '\033[92m'
        defender_color = '\033[94m'
    else:
        attacker_color = '\033[94m'
        defender_color = '\033[92m'
        
    print(f"{attacker_color}{attacker['name']} is attacking {defender_color}{defender['name']}")
    print("")
    
    if attacker['name'] == 'Player':
        player_input = input(f"Press 'R' key and press Enter to roll your 6 sided dice: ")
        element_input = input(f"Press 'E' key and press Enter to roll your 4 sided elemental dice: ")
        print("")
        if player_input != 'r' and player_input != 'R':
            print("")
            print('you have entered an invalid key!')
            attack(attacker, defender)
            return
        if element_input != 'e' and element_input != 'E':
            print("")
            print('you have entered an invalid key!')
            attack(attacker, defender)
            return
        roll = roll_dice()
        eroll_index, eroll_element = elemental_dice()
        print(f"{attacker_color}{attacker['name']} rolls a {roll}")
        print(f"{attacker_color}{attacker['name']} rolls {eroll_element}")
        print("")
    else:
        roll = roll_dice()
        eroll_index, eroll_element = elemental_dice()
        print(f"{attacker_color}{attacker['name']} rolls a {roll}")
        print(f"{attacker_color}{attacker['name']} rolls {eroll_element}")
        print("")

    defense_roll = roll_dice()
    # edefence_roll = elemental_dice()
    print(f"{defender_color}{defender['name']} rolls a {defense_roll}")
    # print(f"{defender_color}{defender['name']} rolls a {edefense_roll}")

    if roll > defense_roll and roll == 20:
        print(f"{attacker_color}{attacker['name']}'s attack lands, its a critical hit!! {defender_color}{defender['name']} loses 40 health.")
        defender['health'] -= 40

    elif roll > defense_roll:
        print(f"{attacker_color}{attacker['name']}'s attack lands! {defender_color}{defender['name']} loses 20 health.")
        defender['health'] -= 20
    else:
        print(f"{defender_color}{defender['name']} blocks the attack!")

    print("")
    print('\033[91m' + f"{attacker['name']} health: {attacker['health']}\033[0m")
    print('\033[91m' + f"{defender['name']} health: {defender['health']}\033[0m")
    print("")

    if eroll_index == 0:
        print(f"{attacker_color}{attacker['name']} does {eroll_element} damage {defender_color}{defender['name']} loses 4 health.")
        defender['health'] -= 4
        print("-------------------------------------------------------------------")
        print('\033[91m' + f"{attacker['name']} health: {attacker['health']}\033[0m")
        print('\033[91m' + f"{defender['name']} health: {defender['health']}\033[0m")
    else:
        print(f"{attacker_color}{attacker['name']}'s elemental damage missed!")
        print("-------------------------------------------------------------------")
    
    # New line after attack session is complete..
    print("")

player = {'name': 'Player', 'health': 300}
enemy = {'name': 'Enemy', 'health': 300}


while player['health'] > 0 and enemy['health'] > 0:
    attack(player, enemy)
    if enemy['health'] <= 0:
        print(f"{enemy['name']} has been defeated!")
        break
    attack(enemy, player)
    if player['health'] <= 0:
        print(f"{player['name']} has been defeated!")
        break