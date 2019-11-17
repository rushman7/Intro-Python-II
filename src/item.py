class Item:
  def __init__(self, name, description, durability):
    self.name = name
    self.description = description
    self.durability = durability

  def __str__(self):
    return f"Item: \033[1;32;49m{self.name}\033[0;37;49m, \033[1;35;49m{self.durability}/100\033[0;37;49m\nDescription:\033[0;34;49m {self.description}\033[0;37;49m"
    
all_items = {
    'sword': Item("Sword", "The sword hums with a strange power.", 100),
    'helmet': Item("Hat", "The most uninteresting helmet you've ever laid eyes upon.", 89),
    'shield': Item("Shield", "The greatest offense is a good defense.", 91),
    'chest': Item("Treasure Chest", "This chest contains the grand gift of knowledge.", 93),
    'armor': Item("Armor", "Protects you from bad people.", 45),
    'spear': Item("Spear", "Sharp ends on this weapon.", 85)
}