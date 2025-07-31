# 🕹️ Tic-Tac-Toe (Console Version)

A simple 2-player **Tic-Tac-Toe** game implemented in Python that runs in the terminal. The game allows two users to play turn-by-turn by entering numbers corresponding to positions on a 3x3 grid.

---

## 📂 File Structure

- `main.py` – Contains all the game logic, including board initialization, move handling, win condition checking, and the main gameplay loop.

---

## ▶️ How to Run

1. Make sure you have Python installed (version 3.6 or higher).
2. Save the code in a file named `main.py`.
3. Run the script in your terminal or command prompt:

```bash
python main.py
```

---

## 🎮 Gameplay Instructions

- At the start, a 3x3 grid is displayed with numbers 1 through 9 representing each cell:
  ```
   1   |   2   |   3
   4   |   5   |   6
   7   |   8   |   9
  ```

- Players will be prompted to choose whether they want to play as `'x'` or `'o'`.

- On each turn, a player selects a cell by entering a number from **1 to 9**.

- The board updates after every move.

- The game continues until one player wins or the board is full (draw).

---

## ✅ Features

- Turn-based 2-player game
- Input validation for moves
- Automatic win and draw detection
- Simple console-based interface

---

## 🛠️ Functions Overview

| Function | Description |
|---------|-------------|
| `initialize_board()` | Creates and returns the initial board. |
| `display_board(board)` | Prints the board in a readable format. |
| `make_move(board, position, player)` | Updates the board based on player's move. |
| `check_winner(board)` | Checks all win conditions (rows, columns, diagonals). |
| `is_board_full(board)` | Returns `True` if the board has no empty spots. |
| `switch_player(current_player)` | Switches the current player between `'x'` and `'o'`. |
| `gameplay()` | The main game loop that handles the flow. |

---

