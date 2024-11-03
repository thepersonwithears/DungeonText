
# DungeonText
A simple Python library for creating text-based adventure games. 

This library provides reusable classes for handling rooms, items, the player, and game logic. 


## Features

- Create Rooms/Locations

     ```forest = Room("Forest", "A dense forest with large trees.")```
- Connect the Rooms to Allow Travel

    ```forest.connect("east", lake, "west", cave)```

- Create Items

    ```sword = Item("sword", "A rusty old sword lies on the ground.")```

- Add Items to Rooms

    ```forest.items.append(sword)```


## Usage/Commands in 1.0

```help``` - Prints full list of commands in game.py file.

```go east``` - Example of travelling.

```look``` - Looks at current location player is in.

```take sword``` - Takes an item if it is in scene.

```inventory``` - Displays inventory.

## Demo

```from dungeontext_lib import Room, Item, Player, Game, Clear


# Create rooms
forest = Room("Forest", "A dense forest with large trees.")
lake = Room("Lake", "A peaceful lake surrounded by tall trees.")
cave = Room("Cave", "A dark and damp cave with a narrow passage.")

# Connect rooms
forest.connect("east", lake, "west", cave)
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


## Roadmap

- Inventory System

- Combat System

- Puzzle System

### Non-Important Roadmap

- Move ```help``` command into util.py

