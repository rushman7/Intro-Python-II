# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, is_light):
    self.name = name
    self.description = description
    self.items = list()
    self.n_to = None
    self.s_to = None
    self.e_to = None
    self.w_to = None
    self.is_light = is_light
      
  def __str__(self):
    return f"Location: \033[0;31;49m{self.name}\033[0;37;49m\nDescription:\033[0;34;49m {self.description}\033[0;37;49m\n---------------------------------------------------------"


room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons", True),
    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", False),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", True),
    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", False),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", False),
    'graveyard': Room('Graveyard', """A dark scary area filled with death. There seems to be a shack towards the northern area.""", True),
    'shack': Room('Shack', """A creepy area filled with multiple old tools, antiques, and spider webs. Nothing else to explore here from here.""", False)
}

