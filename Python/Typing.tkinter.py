import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class TypingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Typing Game")
        self.geometry("400x200")
        self.resizable(False, False)

        self.quote = "Practice makes perfect."
        self.start_time = 0
        self.end_time = 0

        self.quote_label = tk.Label(self, text="Type the following quote: " + self.quote)
        self.quote_label.pack()

        self.input_text = tk.StringVar()
        self.input_entry = tk.Entry(self, textvariable=self.input_text)
        self.input_entry.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.check_input)
        self.submit_button.pack()

    def check_input(self):
        self.end_time = datetime.now()
        input_text = self.input_text.get()
        if input_text == self.quote:
            messagebox.showinfo("Congratulations", "You typed the quote correctly!")
            elapsed_time = (self.end_time - self.start_time).seconds
            wpm = len(self.quote.split()) / (elapsed_time / 60)
            messagebox.showinfo("Result", f"WPM: {round(wpm)}")
            self.destroy()
        else:
            messagebox.showerror("Sorry", "That's not correct. Please try again.")

    def start(self):
        self.start_time = datetime.now()
        self.mainloop()

if __name__ == "__main__":
    game = TypingGame()
    game.start()
