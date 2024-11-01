class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.connections = {}

    def connect(self, *args):
        if len(args) % 2 != 0:
            raise ValueError("Arguments should be provided in direction-room pairs.")

        for i in range(0, len(args), 2):
            direction = args[i]
            room = args[i + 1]
            self.connections[direction] = room

    def __str__(self):
        return f"{self.name}\n{self.description}"
