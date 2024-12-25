import tkinter as tk
from tkinter import messagebox
import random

# List of words to choose from
words = ["python", "java", "javascript", "ruby", "csharp", "php"]

def choose_word():
    return random.choice(words)

def jumble_word(word):
    jumbled = list(word)
    random.shuffle(jumbled)
    return ''.join(jumbled)

class WordJumbleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Jumble Game")
        self.word_to_guess = choose_word()
        self.jumbled_word = jumble_word(self.word_to_guess)

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Guess the word:", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.jumbled_label = tk.Label(self.root, text=self.jumbled_word, font=("Helvetica", 24))
        self.jumbled_label.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer, font=("Helvetica", 16))
        self.submit_button.pack(pady=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game, font=("Helvetica", 16))
        self.reset_button.pack(pady=10)

    def check_answer(self):
        user_guess = self.entry.get()
        if user_guess.lower() == self.word_to_guess:
            messagebox.showinfo("Correct!", "Congratulations! You guessed the word correctly.")
        else:
            messagebox.showerror("Incorrect", "Sorry, that's not correct. Try again!")

    def reset_game(self):
        self.word_to_guess = choose_word()
        self.jumbled_word = jumble_word(self.word_to_guess)
        self.jumbled_label.config(text=self.jumbled_word)
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = WordJumbleGame(root)
    root.mainloop()
