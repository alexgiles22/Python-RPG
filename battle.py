import random
from characters import my_hero, enemy_one, enemy_two,enemy_three
# hero and enemy attacks to be chosen at random

def battle_one():
    pass
    # I want my Hero and/or Enemy's health to decrease based on the opponent's attack power
    """
    1. Get an attack from my Hero 
    2. Get an attack from my Enemy
    3. I want the Hero to attack the Enemy
    4. I want the Enemy to attack the Hero
    5. I want the attack_power from one to reduce the health of the other
    6. I want to check to see if either opponent has lost all of their health
    7. If either one has, I want to finish the battle and declare a winner
    """
# encounter = 1
# while encounter <= 4:
#     battle_one
# while my_hero["health"] >= 0:
#     attack_name, attack_power = random.choice(my_hero["attacks"])
#     e1_attack, e1_power = random.choice(enemy_one["attacks"])
#     print(f"{my_hero['name']} used {attack_name}! It did {attack_power} damage!")
#     enemy_one["health"] -= attack_power
#     print(f"{enemy_one['name']} has {enemy_one['health']} health points left!")
#     print(f"{enemy_one['name']} used {e1_attack} for {e1_power} damage!")
#     my_hero["health"] -= e1_power
#     print(f"{my_hero['name']} has {my_hero['health']} health points left!")
#     if enemy_one["health"] <= 0:
#         print("Battle won! On to the next foe!")

def equipment():
    print(f"{my_hero['name']} collected {enemy_one['equipment']}!")
    my_hero["equipment"].update(enemy_one["equipment"])
    # for key in my_hero["coins"]:
    #     if key in enemy_one["coins"]:
    #         my_hero["coins"] = enemy_one["coins"] + my_hero["coins"]
    #my_hero["coins"].update(enemy_one["coins"])
    my_hero["coins"].update(enemy_one["coins"])
    print(my_hero["equipment"])
    print(my_hero["coins"])
    
    '''
    as a user i want to be able to loot defeated enemies by adding the
    enemy's equipment set to the hero's equipment set
        1. print statement saying hero is looting enemy
        2  use .update() to add enemy equipment to hero equipment
        3. combine coin dictionaries; .update()
        4. print new equipment, and coins
    '''
equipment()

# run_rpg()
#     batt logic()
#       equip()
            # use merge for looting coins?