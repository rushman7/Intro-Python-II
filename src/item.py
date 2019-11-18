class Item:
  def __init__(self, name, description, value):
    self.name = name
    self.description = description
    self.value = value

  def __str__(self):
    return f"Item: \033[1;32;49m{self.name}\033[0;37;49m, \033[1;35;49m{self.value}\033[0;37;49m,\033[0;34;49m {self.description}\033[0;37;49m"
    
all_items = {
    'sword': Item("Sword", "The sword hums with a strange power.", 17),
    'helmet': Item("Helmet", "The most uninteresting helmet you've ever laid eyes upon.", 6),
    'shield': Item("Shield", "The greatest offense is a good defense.", 11),
    'chest': Item("Treasure Chest", "This chest contains the grand gift of knowledge.", 13),
    'armor': Item("Armor", "Protects you from bad people.", 5),
    'spear': Item("Spear", "Sharp ends on this weapon.", 15)
}