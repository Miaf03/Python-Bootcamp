import time
import random
import tkinter as tk

def load_texts():
    """Load phrases from the texts.txt file"""
    with open("texts.txt", "r") as file:
        lines = file.readlines()
        return [line.strip() for line in lines if line.strip()]

def start_test():
    """Start the typing test"""
    global start_time
    text_box.delete("1.0", tk.END)
    chosen_text = random.choice(texts)
    sample_label.config(text=chosen_text)
    start_button.config(state="disabled")
    finish_button.config(state="normal")
    start_time = None
    result_label.config(text="")

def on_typing(event):
    """Start the timer when the user begins typing"""
    global start_time
    if start_time is None:
        start_time = time.time()

def finish_test():
    """Calculate time, accuracy, and typing speed"""
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    
    typed_text = text_box.get("1.0", tk.END).strip()
    original_text = sample_label.cget("text")
    
    # Calculate words per minute (WPM)
    word_count = len(typed_text.split())
    wpm = round((word_count / total_time) * 60, 2)
    
    # Calculate accuracy
    correct_chars = sum(1 for a, b in zip(typed_text, original_text) if a == b)
    total_chars = len(original_text)
    accuracy = round((correct_chars / total_chars) * 100, 2)
    
    # Display results
    result_label.config(
        text=f"Tiempo: {total_time}s | WPM: {wpm} | Precisión: {accuracy}%"
    )
    
    finish_button.config(state="disabled")
    start_button.config(state="normal")
    
# ---------------------------- GUI SETUP ---------------------------- #

window = tk.Tk()
window.title("Typing Speed Test")
window.config(padx=40, pady=40, bg="#000")

texts = load_texts()

sample_label = tk.Label(window, text="Click 'Start' to begin", 
                        wraplength=500, font=("Helvetica", 14), bg="#000", fg="white")
sample_label.pack(pady=20)

text_box = tk.Text(window, width=60, height=10, font=("Courier", 12), wrap="word", 
                   bg="#111", fg="#f8f9fa", insertbackground="white")             

text_box.pack()
text_box.bind("<Key>", on_typing)

button_frame = tk.Frame(window, bg="#000")
button_frame.pack(pady=20)

start_button = tk.Button(button_frame, text="Start", command=start_test, fg="black", width=12)
start_button.grid(row=0, column=0, padx=10)

finish_button = tk.Button(button_frame, text="Finish", command=finish_test, fg="black", width=12)
finish_button.grid(row=0, column=1, padx=10)

result_label = tk.Label(window, text="", font=("Helvetica", 12, "bold"), bg="#000", fg="white")
result_label.pack(pady=10)

window.mainloop()