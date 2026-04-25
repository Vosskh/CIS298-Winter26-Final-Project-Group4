import tkinter as tk
from question_manager import load_questions
from game_logic import GameLogic


class JeopardyGame:
    def __init__(self):
        self.questions = load_questions()
        self.game = GameLogic()
        self.buttons = {}

        self.window = tk.Tk()
        self.window.title("Jeopardy Game")
        self.window.geometry("1000x600")
        self.window.configure(bg="navy")

        self.title_label = tk.Label(
            self.window,
            text="Jeopardy!",
            font=("Arial", 24),
            bg="navy",
            fg="white"
        )
        self.title_label.pack(pady=20)

        self.player1_label = tk.Label(
            self.window,
            text="Player 1 Score: 0",
            font=("Arial", 16),
            bg="navy",
            fg="white"
        )
        self.player1_label.pack()

        self.player2_label = tk.Label(
            self.window,
            text="Player 2 Score: 0",
            font=("Arial", 16),
            bg="navy",
            fg="white"
        )
        self.player2_label.pack()

        self.turn_label = tk.Label(
            self.window,
            text="Current Turn: Player 1",
            font=("Arial", 16),
            bg="navy",
            fg="white"
        )
        self.turn_label.pack(pady=10)

        self.board_frame = tk.Frame(self.window, bg="navy")
        self.board_frame.pack(pady=20)

        self.categories = list(self.questions.keys())
        self.values = [100, 200, 300, 400, 500]

        for col, category in enumerate(self.categories):
            category_label = tk.Label(
                self.board_frame,
                text=category,
                font=("Arial", 14, "bold"),
                width=15,
                height=2,
                borderwidth=1,
                relief="solid",
                bg="blue",
                fg="white"
            )
            category_label.grid(row=0, column=col)

            for row, value in enumerate(self.values, start=1):
                button = tk.Button(
                    self.board_frame,
                    text=str(value),
                    font=("Arial", 14),
                    width=15,
                    height=2,
                    bg="blue",
                    fg="white",
                    command=lambda c=category, v=value: self.show_question(c, v)
                )
                button.grid(row=row, column=col)
                self.buttons[(category, value)] = button

    def show_question(self, category, value):
        question_data = None

        for question in self.questions[category]:
            if question["value"] == value:
                question_data = question
                break

        if question_data:
            question_window = tk.Toplevel(self.window)
            question_window.title(f"{category} - {value}")
            question_window.geometry("500x400")
            question_window.configure(bg="navy")

            question_label = tk.Label(
                question_window,
                text=question_data["question"],
                font=("Arial", 16),
                wraplength=450,
                bg="navy",
                fg="white"
            )
            question_label.pack(pady=20)

            answer_entry = tk.Entry(question_window, font=("Arial", 14), width=30)
            answer_entry.pack(pady=10)

            result_label = tk.Label(
                question_window,
                text="",
                font=("Arial", 14),
                bg="navy",
                fg="white"
            )
            result_label.pack(pady=10)

            submit_button = tk.Button(
                question_window,
                text="Submit Answer",
                font=("Arial", 14),
                command=lambda: self.check_answer(
                    question_data["answer"],
                    answer_entry.get(),
                    value,
                    result_label,
                    question_window,
                    category
                )
            )
            submit_button.pack(pady=10)

    def check_answer(self, correct_answer, user_answer, value, result_label, question_window, category):
        if user_answer.lower().strip() == correct_answer.lower().strip():
            self.game.add_points(value)
            result_label.config(text="Correct!")
        else:
            result_label.config(text=f"Wrong! Correct answer: {correct_answer}")

        player1_score, player2_score = self.game.get_scores()
        self.player1_label.config(text=f"Player 1 Score: {player1_score}")
        self.player2_label.config(text=f"Player 2 Score: {player2_score}")

        self.buttons[(category, value)].config(state="disabled")

        self.game.switch_turn()
        current_player = self.game.get_current_player()
        self.turn_label.config(text=f"Current Turn: Player {current_player}")

    def run(self):
        self.window.mainloop()


app = JeopardyGame()
app.run()