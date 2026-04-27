# CIS-298-Winter-26-Final-Project-Group-4

## Project Pitch & Overview
For our final project, we developed a fully functional, two-player interactive **Jeopardy!** game using Python. The objective was to build a desktop graphical user interface (GUI) that seamlessly handles game state, user input validation, and dynamic data parsing. We utilized the built-in `tkinter` library for the visual interface and the `json` library to manage our trivia database. 

## Functionality
This program includes the following features:
* **Interactive GUI Board:** A customized `tkinter` window displaying a 5x5 grid of clickable point values across five unique categories (Sports, Movies, Music, Video Games, TV Shows).
* **Dynamic Data Loading:** Trivia categories, questions, and answers are cleanly separated from the main logic and loaded dynamically via `question_manager.py` from `questions.json`.
* **Two-Player State Management:** `game_logic.py` tracks the current player's turn, automatically switching between Player 1 and Player 2 after each attempted question, and maintains independent running scores.
* **Input Validation & Feedback:** When a question is clicked, a popup window prompts the user for an answer. The program checks the user's input against the correct answer (ignoring case sensitivity and extra spaces) and displays immediate "Correct!" or "Wrong!" feedback.
* **Button Disabling:** To prevent questions from being answered multiple times, point value buttons on the main board are dynamically disabled once they have been clicked.

## How to Run
1. Ensure you have Python 3.x installed (no external `pip` packages are required as `tkinter` and `json` are built-in).
2. Download or clone all files into the same directory (`jeopardy_game.py`, `game_logic.py`, `question_manager.py`, `questions.json`).
3. Run the main application file:
   ```bash
   python jeopardy_game.py
