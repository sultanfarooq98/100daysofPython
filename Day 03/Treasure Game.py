print("Welcome to Treasure island game")
# print('''       ____...------------...____
#                _.-"` /o/__ ____ __ __  __ \o\_`"-._
#              .'     / /                    \ \     '.
#              |=====/o/======================\o\=====|
#              |____/_/________..____..________\_\____|
#              /   _/ \_     <_o#\__/#o_>     _/ \_   
#              \_________\####/_________/
#               |===\!/========================\!/===|
#               |   |=|          .---.         |=|   |
#               |===|o|=========/     \========|o|===|
#               |   | |         \() ()/        | |   |
#               |===|o|======{'-.) A (.-'}=====|o|===|
#               | __/ \__     '-.\uuu/.-'    __/ \__ |
#               |==== .'.'^'.'.====|
#           jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
#               `""""-""""""""""""""""""""""""""-""""` ''')


choose = input("Choose: left or right? ").lower()

if choose == "left":
    c2 = input("Choose: swim or wait : ").lower()
    if c2 == "wait":
        c3 = input("Choose: Which door blue, red, yellow : ").lower()
        if c3 == "yellow":
            print("You Win")
        elif c3 == "red":
            print("Burned by fire GAME OVER")
        elif c3 == "blue":
            print("Eaten by beasts GAME OVER")
    else:
        print("Attack by trout GAME OVER")
else:
    print("Game Over")

