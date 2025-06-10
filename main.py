import tkinter as tk
from game import Game
from screen import Screen
from style import Style

if __name__ == "__main__":
    root = tk.Tk()
    game = Game()
    screen = Screen(root, game)
    screen.schedule()
    style = Style()
    root.mainloop()
