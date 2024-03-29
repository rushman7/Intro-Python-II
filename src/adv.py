from room import Room, room
from player import Player
from item import all_items

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['graveyard']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['graveyard'].n_to = room['shack']
room['graveyard'].e_to = room['foyer']
room['shack'].s_to = room['graveyard']

# Add items to rooms

room['outside'].items = [all_items['sword'], all_items['shield']]
room['overlook'].items = [all_items['chest']]
room['narrow'].items = [all_items['armor']]
room['shack'].items = [all_items['spear'], all_items['helmet']]
room['graveyard'].items = [all_items['gold']]
room['treasure'].items = [all_items['diamond'], all_items['ruby'], all_items['emerald']]

# Main

player = Player('Jack Sparrow', room['outside'], [all_items['lamp']], 0)

# player = Player(input("\nWhat is yourname?:"), room['outside'], [])
print(f"Welcome \033[1;32;49m{player.name}\033[0;37;49m!")

playing = True

while(playing):
    print(player)

    if player.score == 100:
        print("\033[1;32;49mCongratulations you beat the game! Exiting now...")
        break

    inp = input("\nType h for a list of commands\nPlease input a command: ")

    if inp.lower() == 'q':
        print("\033[1;31;49mExiting Game...")
        break
    elif inp.lower() == 'n':
        if player.current_room.n_to == None:
           print(f"\x1b[1;31;40m\nYou cannot move in that direction\x1b[0m\n") 
        else:
            player.current_room = player.current_room.n_to
    elif inp.lower() == 's':
        if player.current_room.s_to == None:
           print(f"\x1b[1;31;40m\nYou cannot move in that direction\x1b[0m\n") 
        else:
            player.current_room = player.current_room.s_to
    elif inp.lower() == 'e':
        if player.current_room.e_to == None:
           print(f"\x1b[1;31;40m\nYou cannot move in that direction\x1b[0m\n") 
        else:
            player.current_room = player.current_room.e_to
    elif inp.lower() == 'w':
        if player.current_room.w_to == None:
           print(f"\x1b[1;31;40m\nYou cannot move in that direction\x1b[0m\n") 
        else:
            player.current_room = player.current_room.w_to
    elif inp.lower() == 'p':
        player.add_to_inventory()
    elif inp.lower() == 'i':
        player.open_inventory()
    elif inp.lower() == 'c':
        player.search()
    elif inp.lower() == 'd':
        player.remove_from_inventory()
    elif inp.lower() == 'h':
        print('\033[1;32;49mh -> list of commands')
        print('n -> player moves north')
        print('s -> player moves south')
        print('e -> player moves east')
        print('w -> player moves west')
        print('p -> pick up item in area')
        print('i -> open inventory')
        print('c -> search the area for items')
        print('d -> drop item in area\033[0;37;49m')
