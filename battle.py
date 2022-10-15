import random
from characters import my_hero, enemy_one, enemy_two,enemy_three
# hero and enemy attacks to be chosen at random

def battle(enemy_passed):
    while enemy_passed["health"] >= 0:
        attack_name, attack_power = random.choice(my_hero["attacks"])
        e_attack, e_power = random.choice(enemy_passed["attacks"])
        print(f"{my_hero['name']} used {attack_name}! It did {attack_power} damage!")
        enemy_passed["health"] -= attack_power
        print(f"{enemy_passed['name']} used {e_attack} for {e_power} damage!")
        my_hero["health"] -= e_power
        print(f"{my_hero['name']} has {my_hero['health']} health points left!")
        print(f"{enemy_passed['name']} has {enemy_passed['health']} health points left!")
        if enemy_passed["health"] <= 0:
            print("Battle won!")
            my_hero["level"] += 1
            print(f"{my_hero['name']} is now level {my_hero['level']}!")
            break
        elif my_hero["health"] <= 0:
            input(f"Oh no! {my_hero['name']} lost! Would you like to try again? Y/N")
            if input == "Y":
                run_game()
            elif input != "Y":
                input("I didn't get that, could you try again? Y/N")

def equipment(enemy_passed):
    print(f"{my_hero['name']} collected {enemy_passed['equipment']}!")
    my_hero["equipment"].update(enemy_passed["equipment"])

def coins(enemy_passed):    
    my_hero["coins"]["copper"] += enemy_passed["coins"]["copper"]
    my_hero["coins"]["silver"] += enemy_passed["coins"]["silver"]
    my_hero["coins"]["gold"] += enemy_passed["coins"]["gold"]
    
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