# game.py
from .room import Room
from .item import Item
from .player import Player

class Game:
    def __init__(self, player):
        self.player = player

    def interpret(self, command):
        if command.startswith("go "):
            direction = command.split(" ")[1]
            self.player.move(direction)
        elif command == "look":
            print(self.player.current_room)
        elif command.startswith("take "):
            item_name = command.split(" ")[1]
            self.take_item(item_name)

    def take_item(self, item_name):
        item = next((i for i in self.player.current_room.items if i.name == item_name), None)
        if item:
            self.player.inventory.append(item)
            self.player.current_room.items.remove(item)
            print(f"You take the {item_name}.")
        else:
            print(f"No {item_name} here.")

