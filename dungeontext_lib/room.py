# room.py
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.connections = {}

    def connect(self, direction, room):
        self.connections[direction] = room

    def __str__(self):
        return f"{self.name}\n{self.description}"
