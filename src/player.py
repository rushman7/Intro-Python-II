# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room

  def __str__(self):
    return f"\033[1;32;49m{self.name} \033[0;37;49mis currently in: \n{self.current_room}"
