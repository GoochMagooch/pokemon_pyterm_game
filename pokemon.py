class Pokemon:
  health = 100

  def __init__(self, name, attack_name, pokemon_type):
    self.name = name
    self.attack_name = attack_name
    self.pokemon_type = pokemon_type

  def __repr__(self):
    return(f"Pokemon name: {self.name}\n"
           f"Pokemon type: {self.pokemon_type}\n"
           f"Pokemon attack: {self.attack_name}\n"
           f"Pokemon health: {self.health}")

  def knockout(self):
    is_knocked_out = True
    self.health = 0

  def attack(self, enemy):
      if (self.pokemon_type == "water" and enemy.pokemon_type == "fire") or (self.pokemon_type == "fire" and enemy.pokemon_type == "plant") or (self.pokemon_type == "electric" and enemy.pokemon_type == "water"):
        enemy.health -= 25
        if enemy.health <= 0:
          enemy.knockout()
          print(f"{enemy.name} has been knocked out!")
        else:
          print(f"{self.name} attacks {enemy.name} with {self.attack_name}")
          print("It is super effective!")
          print(f"{enemy.name}'s health is now: {enemy.health}")
      else:
        enemy.health -= 10
        print(f"{self.name} attacks {enemy.name} with {self.attack_name}")
        print("It is not very effective!")
        print(f"{enemy.name}'s health is now: {enemy.health}")

class Trainer:
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return(f"My name is {self.name}!")

  def revive(self, pokemon):
    if type(pokemon) == Pokemon:
      pokemon.health = 25
      print(f"{pokemon.name} has been revived with 25 health points!")
    else:
      print("This pokemon is not part of your list!")

  def potion(self, pokemon):  
    if self.pokemon > 50:
      diff = 100 - pokemon.health
      pokemon.health = 100
      return(f"{pokemon.name} has received a {diff}HP increase and is now at full health!")
    new_health = pokemon.health + 50
    pokemon.health += 50
    return(f"{pokemon.name} has received a 50HP increase for a new HP level of {new_health}!")




'''
bulbasaur = Pokemon("Bulbasaur", "water gun", "water")
pikachu = Pokemon("Pikachu", "thunderbolt", "electric")
chimchar = Pokemon("Chimchar", "ember", "fire")
'''