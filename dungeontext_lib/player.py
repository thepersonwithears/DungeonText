from .utils import Clear

class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.connections:
            self.current_room = self.current_room.connections[direction]
            Clear()
            print(f"You move to the {self.current_room.name}")
        else:
            Clear()
            print("You can't go that way.")
