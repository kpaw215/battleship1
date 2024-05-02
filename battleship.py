Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Importing libraries
... import random
... 
... # Initializing the game board
... board = [[0 for _ in range(10)] for _ in range(10)]
... 
... # Placing ships on the board
... def place_ships():
...     for i in range(5):
...         x = random.randint(0, 9)
...         y = random.randint(0, 9)
...         board[x][y] = 1
... 
... # Function to check hits
... def check_hit(x, y):
...     if board[x][y] == 1:
...         return True
...     else:
...         return False
... 
... # Setting up the game
