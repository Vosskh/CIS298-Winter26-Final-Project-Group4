# CIS-298 Winter26_Final Project Group4

## Overview

We developed a fully functional, interactive Jeopardy game using Python. The objective was to build a desktop graphical user interface (GUI) that seamlessly handles game state, user input validation, and dynamic data parsing. We utilized the built-in `tkinter` library for the visual interface and the `json` library to manage our trivia database. 



## Functionality

This program includes the following features:

* **Interactive GUI Board:** A customized `tkinter` window displaying a 5x5 grid of clickable point values across five unique categories (Sports, Movies, Music, Video Games, TV Shows).
* **Dynamic Data Loading:** Trivia categories, questions, and answers are cleanly separated from the main logic and loaded dynamically via `question_manager.py` from `questions.json`.
* **Two-Player State Management:** `game_logic.py` tracks the current player's turn, automatically switching between Player 1 and Player 2 after each attempted question, and maintains independent running scores.
* **Input Validation & Feedback:** When a question is clicked, a popup window prompts the user for an answer. The program checks the user's input against the correct answer (ignoring case sensitivity and extra spaces) and displays immediate "Correct!" or "Wrong!" feedback.
* **Button Disabling:** To prevent questions from being answered multiple times, point value buttons on the main board are dynamically disabled once they have been clicked.



## Team Evaluations

All individual team evaluations have been committed directly to this GitHub repository by each team member.



## Development Log

Below is the log of our regular git commits spanning a 10-day period. This details the time spent and the specific accomplishments for each phase of development.

**Total Estimated Time Spent: 55 Hours**

| Commit # | Date  | Time Spent | What was done                                                |
| :------- | :---- | :--------- | :----------------------------------------------------------- |
| **1**    | 04/18 | 4 hours    | Created the repository, planned the project idea, and set up the basic file structure for the Jeopardy game. |
| **2**    | 04/19 | 5 hours    | Created .gitignore, started the Python project files, and built the first versions of question_manager.py and game_logic.py to separate question loading from game rules. |
| **3**    | 04/20 | 9 hours    | Built the first draft of questions.json with 5 categories and point-based questions, and tested loading the JSON data into Python. |
| **4**    | 04/21 | 9 hours    | Developed the main tkinter interface in jeopardy_game.py, including the main window, title label, player score labels, current turn label, and board frame. |
| **5**    | 04/22 | 4.5 hours  | Added category headers and clickable point buttons to the Jeopardy board, and connected each button to the correct category and value. |
| **6**    | 04/23 | 5 hours    | Added the question popup window, answer text box, submit button, and logic to check whether the typed answer matched the correct answer from the JSON file. |
| **7**    | 04/24 | 4 hours    | Connected answer checking to the score system, updated Player 1 and Player 2 scores, and added automatic turn switching after each question. |
| **8**    | 04/25 | 5 hours    | Disabled used buttons after questions were answered, finalized the main gameplay behavior, added comments, and cleaned up wording and formatting in the code and question file. |
| **9**    | 04/26 | 4.5 hours  | Performed final bug fixes and testing, improved the question bank, cleaned up the UI, and checked that the game worked correctly from start to finish. |
| **10**   | 04/27 | 5 hours    | Completed the README with the project pitch, feature list, how-to-run section, screenshots, and the final commit/time log for submission. |
