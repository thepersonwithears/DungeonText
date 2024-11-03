import os

clear_screen = True

def Clear():
    if clear_screen:
        os.system('cls' if os.name == 'nt' else 'clear')

def Commands():
    print("Commands:")
    print("go <direction> - Move to a different room")
    print("look - Look around the current room")
    print("take <item> - Take an item from the current room")
    print("help - Show this help message")