# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room, inventory, score):
    self.name = name
    self.current_room = current_room
    self.inventory = inventory
    self.score = score

  def __str__(self):
    return f"Current Score:\033[1;36;49m {self.score}/67\n\033[0;37;49m{self.current_room}"

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
    else:
      item_choice = input('There are multiple items in this area, which would you like to pick up: ')
      for item in self.current_room.items:
        if item_choice.lower() == item.name.lower():
          self.inventory.append(item)
          self.score += item.value
          self.current_room.items.remove(item)
          print(f"\033[1;32;49mYou have picked up \033[1;32;49m{item.name}\033[0;37;49m")

  def remove_from_inventory(self):
    if len(self.inventory) <= 0:
      print('\033[0;31;49mThere are no items in your inventory')
    else:
      item_choice = input('There are multiple items in this area, which would you like to drop: ')
      for item in self.inventory:
        if item_choice.lower() == item.name.lower():
          self.inventory.remove(item)
          self.score -= item.value
          self.current_room.items.append(item)
          print(f"You have dropped the \033[1;32;49m{item.name} in \033[0;31;49m{self.current_room}")

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