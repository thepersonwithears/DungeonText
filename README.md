# DungeonText

A simple Python library for creating text-based adventure games. This library provides reusable classes for handling rooms, items, the player, and game logic. It’s designed to be easily extensible, so you can add custom game elements and interactions.


## Installation

Clone the repository and navigate to the main project folder (where `setup.py` is located). Then, install the library locally using:

```bash
pip install -e .

```

## Sample Code - Demonstrates all modules and functions!

```
from dungeontext_lib import Room, Item, Player, Game, Clear


# Create rooms
forest = Room("Forest", "A dense forest with towering trees.")
lake = Room("Lake", "A peaceful lake surrounded by tall trees.")

# Connect rooms
forest.connect("east", lake)
lake.connect("west", forest)

# Create items
sword = Item("sword", "A rusty old sword lies on the ground.")

# Adding items to rooms
forest.items.append(sword)

# Initialize player and gameo
player = Player(start_room=forest)
game = Game(player)

# Main loop
while True:
    command = input("> ")
    if command in ("quit", "exit"):
        Clear()
        print("Goodbye!")
        break
    game.interpret(command)
```
