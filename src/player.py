# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room

  def __str__(self):
    return f"\033[1;32;49m{self.name} \033[0;37;49mis currently in: \n{self.current_room}"

  def search(self):
    if len(self.current_room.items) <= 0:
      print('--------\033[1;36;49mItems in Area\033[0;37;49m--------\n\033[0;31;49m    No items in this room\033[0;37;49m\n-----------------------------')
    else:
      print('--------\033[1;36;49mItems in Area\033[0;37;49m--------')
      for item in self.current_room.items:
        print(item)
      print('-----------------------------')
