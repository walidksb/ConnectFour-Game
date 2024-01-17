# Connect Four Game

Connect Four is a classic two-player connection game where players aim to connect four discs of the same color vertically, horizontally, or diagonally before their opponent.

## Features

- **Minimax Algorithm:** Implemented an AI player using the minimax algorithm with alpha-beta pruning for decision making.
- **Heuristic Evaluation:** Utilized heuristic functions to evaluate the game state and guide the AI's decision-making process.
- **Flexible Board Size:** Supports a customizable grid size to adapt the game to different preferences.
- **Web-based Interface:** Enjoy a modern and dynamic gaming experience with a user-friendly interface developed using React.
- **Real-time Multiplayer:** Play against friends or other players in real-time with the help of WebSockets.

## How to Play

1. Choose a color for each player.
2. Players take turns dropping one colored disc from the top into a vertically suspended grid.
3. The object is to connect four discs of the same color consecutively vertically, horizontally, or diagonally before the opponent.

## Configuration:

1. **Clone the repo:**
   ```
   git clone https://github.com/walidksb/ConnectFourGamev1
   cd ConnectFourGamev1
   ```
2. **Install all dependencies:**
      ```
   npm install
   pip install -r requirements.txt
      ```
3. **Create a local .env file:**
   * For Linux:
      ```
     cp .env.example .env
      ```
   * For Windows:
      ```
     copy .env.example .env
      ```
## Usage:
1. **Run the Front part:**
   ```
     cd client
     npm start
   ```
2. **Run the Back part:**
   ```
     cd flask-server
     ./venv/Scripts/Activate
     python app.py
   ```
## Authors

creators and maintainers

-   [walidksb](https://github.com/walidksb)
-   [kameliabouamara](https://github.com/kameliabouamara)
