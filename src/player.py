# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room, inventory):
    self.name = name
    self.current_room = current_room
    self.inventory = inventory

  def __str__(self):
    return f"{self.current_room}"

  def search(self):
    if len(self.current_room.items) <= 0:
      print('----------------------\033[1;36;49mItems in Area\033[0;37;49m----------------------\n\033[0;31;49m                  No items in this area\033[0;37;49m\n---------------------------------------------------------')
    else:
      print('----------------------\033[1;36;49mItems in Area\033[0;37;49m----------------------')
      for item in self.current_room.items:
        print(item)
      print('---------------------------------------------------------')
  
  def add_to_inventory(self):
    if len(self.current_room.items) <= 0:
      print('\033[0;31;49mThere is no item to add')
    elif len(self.current_room.items) == 1: 
      for item in self.current_room.items:
        self.inventory.append(item)
        self.current_room.items.remove(item)
        print(f"\033[1;32;49m{item.name} has been added to your inventory")
    else:
      for item in self.current_room.items:
        inp = input(f'Do you want to pick up the {item.name}, y/n: ')
        if inp.lower() == 'y':
          self.inventory.append(item)
          self.current_room.items.remove(item)
          print(f"\033[1;32;49m{item.name} has been added to your inventory")
        else: 
          pass

  def open_inventory(self):
    if len(self.inventory) == 0:
      print('-----------------------\033[1;36;49mInventory\033[0;37;49m-------------------------')
      print('\033[0;31;49m          There are no items in your inventory')
      print('\033[0;37;49m---------------------------------------------------------')
    else:
      print('-----------------------\033[1;36;49mInventory\033[0;37;49m-------------------------')
      for item in self.inventory:
        print(item)
      print('\033[0;37;49m---------------------------------------------------------')
