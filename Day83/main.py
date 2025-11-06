import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg="#222")

        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []

        self.create_board()
        self.create_reset_button()

    def create_board(self):
        frame = tk.Frame(self.root, bg="#222")
        frame.pack(pady=20)

        for i in range(9):
            button = tk.Button(
                frame,
                text=" ",
                font=("Arial", 28, "bold"),
                width=5,
                height=2,
                bg="#333",
                fg="white",
                activebackground="#555",
                command=lambda i=i: self.make_move(i)
            )
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

    def create_reset_button(self):
        reset_btn = tk.Button(
            self.root,
            text="Reset Game",
            font=("Arial", 14, "bold"),
            bg="#FFB800",
            fg="#222",
            relief="flat",
            command=self.reset_game
        )
        reset_btn.pack(pady=10)

    def make_move(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(
                text=self.current_player,
                fg="#E74C3C" if self.current_player == "X" else "#3498DB"
            )

            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.disable_buttons()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        return any(all(self.board[i] == player for i in combo) for combo in win_combinations)

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        for button in self.buttons:
            button.config(text=" ", state="normal", fg="white")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()