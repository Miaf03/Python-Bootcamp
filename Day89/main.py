import tkinter as tk
from tkinter import messagebox

TITLE_FONT = "Arial"
ACCENT = "#00FF99"
WORD_FONT = "Consolas"
TEXT_COLOR = "#EEEEEE"
BACKGROUND = "#181C21"
TITLE_COLOR = "#00ADB5"

TIMEOUT = 5

class TypeFlowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Type Flow App")
        self.root.config(padx=25, pady=25, bg=BACKGROUND)
        self.root.geometry("700x500")

        self.current_text = ""
        self.count = TIMEOUT
        self.timer = None

        self.title_label = tk.Label(
            text="Type Flow App",
            font=(TITLE_FONT, 42, "bold"),
            fg=TITLE_COLOR,
            bg=BACKGROUND
        )
        self.title_label.pack(pady=15)

        self.message_label = tk.Label(
            text="Start typing!",
            font=(WORD_FONT, 20),
            fg=TEXT_COLOR,
            bg=BACKGROUND
        )
        self.message_label.pack(pady=10)

        self.text = tk.Text(
            wrap="word",
            font=(WORD_FONT, 15),
            fg=TEXT_COLOR,
            bg="#31363F",
            insertbackground=ACCENT,
            relief="flat",
            height=12,
            width=70,
            padx=15,
            pady=15
        )
        self.text.pack(pady=15)
        self.text.focus()

        self.text.bind("<Key>", self.reset_timer)

        self.check_text()

    def check_text(self):
        typed_text = self.text.get("1.0", tk.END).strip()

        if typed_text == self.current_text and len(typed_text) > 0:
            self.message_label.config(text=f"Deleting in: {self.count}s", fg="#ff4444")
            if self.count == 0:
                self.text.delete("1.0", tk.END)
                self.message_label.config(text="Start again...", fg=TEXT_COLOR)
                self.count = TIMEOUT
            else:
                self.count -= 1
        else:
            self.current_text = typed_text
            self.count = TIMEOUT
            self.message_label.config(text="Keep going!", fg=ACCENT)

        self.root.after(1000, self.check_text)

    def reset_timer(self, event=None):
        self.count = TIMEOUT
        self.current_text = self.text.get("1.0", tk.END).strip()
        self.message_label.config(text="Typing...", fg=ACCENT)


if __name__ == "__main__":
    root = tk.Tk()
    app = TypeFlowApp(root)
    root.mainloop()