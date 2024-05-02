Battleships Game
This is a simple battleships game where the user can click on the game board to send coordinates for hit checking. The game board is displayed as a grid with 10 columns and 10 rows.

How to Play
Open the index.html file in your browser.
Click on any square on the game board to send coordinates for hit checking.
The result of the hit will be displayed on the game board.

Files
index.html: Contains the HTML structure of the game board.
style.css: Contains the CSS styling for the game board.
script.js: Contains the JavaScript code for sending user input to the Python backend for hit checking.
script.py: Contains the Python backend code for initializing the game board, placing ships, and checking hits.
Enjoy the game!

Description
This Battleships game consists of two main parts: the frontend implemented in HTML, CSS, and JavaScript, and the backend implemented in Python. Here is a breakdown of how each part works:

Frontend (HTML, CSS, JavaScript)
HTML: The index.html file sets up the structure of the game board within a div element with the id board.
CSS: The style.css file styles the game board using CSS Grid to create a 10x10 grid with cells of 30px by 30px.
JavaScript: The script.js file contains an event listener that captures user clicks on the game board, calculates the coordinates of the click, and sends them to the Python backend for hit checking.
Backend (Python)
Python: The script.py file initializes a 10x10 game board with all values set to 0. It then randomly places 5 ships on the board by setting their positions to 1.
Placing Ships: The place_ships() function randomly selects coordinates on the board and sets the value to 1 to indicate a ship is present.
Checking Hits: The check_hit(x, y) function checks if there is a ship at the specified coordinates (x, y) on the board and returns True if a ship is hit, else False.
Game Setup: The Python backend sets up the game board and ship placements to interact with the user input from the frontend.
By combining the frontend and backend code, this Battleships game allows users to click on the game board to interact with the Python backend for hit checking and game progression.
