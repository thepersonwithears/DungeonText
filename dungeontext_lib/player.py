# player.py
class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.connections:
            self.current_room = self.current_room.connections[direction]
            print(f"You move to the {self.current_room.name}")
        else:
            print("You can't go that way.")
