from dungeontext_lib import Room, Item, Player, Game, Clear


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