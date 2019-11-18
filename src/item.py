class Item:
  def __init__(self, name, description, value):
    self.name = name
    self.description = description
    self.value = value

  def __str__(self):
    return f"Item: \033[1;32;49m{self.name}\033[0;37;49m, \033[1;35;49m{self.value}\033[0;37;49m,\033[0;34;49m {self.description}\033[0;37;49m"

class LightSource(Item):
  def __init__(self, name, description, value, is_light):
    super().__init__(name, description, value)
    self.is_light = is_light
    
all_items = {
    'sword': Item("Sword", "The sword hums with a strange power.", 7),
    'helmet': Item("Helmet", "The most uninteresting helmet you've ever laid eyes upon.", 3),
    'shield': Item("Shield", "The greatest offense is a good defense.", 6),
    'chest': Item("Treasure Chest", "This chest contains the grand gift of knowledge.", 8),
    'armor': Item("Armor", "Protects you from bad people.", 5),
    'spear': Item("Spear", "Sharp ends on this weapon.", 5),
    'lamp': LightSource("Lamp", "Traversing a pitch black dungeon without light is dangerous.", 0, True)
}