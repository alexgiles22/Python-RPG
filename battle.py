import random
from characters import my_hero, enemy_one, enemy_two,enemy_three
# hero and enemy attacks to be chosen at random

def battle(enemy_passed):
    while enemy_passed["health"] >= 0:
        attack_name, attack_power = random.choice(my_hero["attacks"])
        e_attack, e_power = random.choice(enemy_passed["attacks"])
        print(f"{my_hero['name']} used {attack_name}! It did {attack_power} damage!")
        enemy_passed["health"] -= attack_power
        print(f"{enemy_passed['name']} has {enemy_passed['health']} health points left!")
        print(f"{enemy_passed['name']} used {e_attack} for {e_power} damage!")
        my_hero["health"] -= e_power
        print(f"{my_hero['name']} has {my_hero['health']} health points left!")
        if enemy_passed["health"] <= 0:
            print("Battle won!")
            break

    """
    1. Get an attack from my Hero 
    2. Get an attack from my Enemy
    3. I want the Hero to attack the Enemy
    4. I want the Enemy to attack the Hero
    5. I want the attack_power from one to reduce the health of the other
    6. I want to check to see if either opponent has lost all of their health
    7. If either one has, I want to finish the battle and declare a winner
    """

def equipment(enemy_passed):
    print(f"{my_hero['name']} collected {enemy_passed['equipment']}!")
    my_hero["equipment"].update(enemy_passed["equipment"])
    print(my_hero["equipment"])

def coins(enemy_passed):    
    my_hero["coins"]["copper"] += enemy_passed["coins"]["copper"]
    my_hero["coins"]["silver"] += enemy_passed["coins"]["silver"]
    my_hero["coins"]["gold"] += enemy_passed["coins"]["gold"]
    print(my_hero["coins"])
    
    '''
    as a user i want to be able to loot defeated enemies by adding the
    enemy's equipment set to the hero's equipment set
        1. print statement saying hero is looting enemy
        2  use .update() to add enemy equipment to hero equipment
        3. combine coin dictionaries; .update()
        4. print new equipment, and coins
    '''
def run_game():
    battle(enemy_one)
    equipment(enemy_one)
    coins(enemy_one)
    battle(enemy_two)
    equipment(enemy_two)
    coins(enemy_two)
    battle(enemy_three)
    equipment(enemy_three)
    coins(enemy_three)

run_game()