import os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

class Pokemon:
  health = 100
  is_knocked_out = False

  def __init__(self, name, attack_name, pokemon_type):
    self.name = name
    self.attack_name = attack_name
    self.pokemon_type = pokemon_type

  def __repr__(self):
    return(f"Pokemon name: {self.name}\n"
           f"Pokemon type: {self.pokemon_type}\n"
           f"Pokemon attack: {self.attack_name}\n"
           f"Pokemon health: {self.health}")

  def knockout(self, pokemon):
    pokemon.is_knocked_out = True
    self.health = 0
    print(f"{pokemon.name} has been knocked out!")

  def attack(self, enemy):
    if (self.pokemon_type == "water" and enemy.pokemon_type == "fire") or (self.pokemon_type == "fire" and enemy.pokemon_type == "plant") or (self.pokemon_type == "electric" and enemy.pokemon_type == "water"):
      if enemy.health <= 25:
        enemy.knockout(enemy)
      else:
        new_health = enemy.health - 25
        print(f"{self.name} attacks {enemy.name} with {self.attack_name}")
        print("It is super effective!")
        print(f"{enemy.name}'s health is now: {new_health}")
        enemy.health = new_health
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
    if pokemon.is_knocked_out == True:
      print(f"{pokemon.name} is knocked out!")
    elif pokemon.health > 50:
      diff = 100 - pokemon.health
      pokemon.health = 100
      print(f"{pokemon.name} has received a {diff}HP increase and is now at full health!")
    else:
      new_health = pokemon.health + 50
      pokemon.health += 50
      print(f"{pokemon.name} has received a 50HP increase for a new HP level of {new_health}!")

# Terminal Menu
while True:

  # Trainer One creation
  player_one = input("Player 1 enter your trainer name: ")
  trainer_one = Trainer(player_one)
  print(f"Hello {trainer_one.name}")
  input("Press enter to continue...")
  clear_screen() # Clears screen after a choice is made
  # Trainer Two creation
  player_two = input("Player 2 enter your trainer name: ")
  trainer_two = Trainer(player_two)
  print(f"Hello {trainer_two.name}")
  input("Press enter to continue...")
  clear_screen() # Clears screen after a choice is made
  
  # Trainer One pokemon creation
  pokemon1 = input(f"{trainer_one.name} enter your pokemon: ")
  attack1 = input("Enter your pokemon's attack: ")
  type1 = input("Enter your pokemon's type: ")
  pokemon_one = Pokemon(pokemon1, attack1, type1)
  clear_screen()
  print(f"{trainer_one.name}'s pokemon stats:\n{pokemon_one}\n")
  input("Press enter to continue...")
  clear_screen()
  # Trainer Two pokemon creation
  pokemon2 = input(f"{trainer_two.name} enter your pokemon: ")
  attack2 = input("Enter your pokemon's attack: ")
  type2 = input("Enter your pokemon's type: ")
  print(f"{trainer_two.name}'s pokemon stats:\n{pokemon2}")
  pokemon_two = Pokemon(pokemon2, attack2, type2)
  clear_screen()
  print(f"{trainer_two.name}'s pokemon stats:\n{pokemon_two}\n")
  input("Press enter to continue...")
  clear_screen()

  def battle():
    while True:
      choice = input(f"press 1 to attack\npress 2 to use a potion\npress 3 to revive\nchoice: ")
      if choice == '1':
        clear_screen()
        pokemon_one.attack(pokemon_two)
      elif choice == '2':
        clear_screen()
        trainer_two.potion(pokemon_two)
      elif choice == '3':
        clear_screen()
        trainer_two.revive(pokemon_two)
      elif choice == 'exit':
        print("Exiting stats menu...")
        clear_screen()
        break
      else:
        clear_screen()
        print("Invalid choice...")
      input("Press enter to continue")
      clear_screen()
  battle()