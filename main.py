import tkinter as tk

increment = 1
coins = 0

def coinIncrement():
    global coins
    coins += increment
    coinsLabel.config(text=coins)
    root.after(1000, coinIncrement)

def tryBuy(cost):
    # code

root = tk.Tk()
root.title("Coin Generation")
root.geometry("600x600")

root.after(1000, coinIncrement)

coinsLabel = tk.Label(root, text=coins)
coinsLabel.pack()

incrementLabel = tk.Label(root, text=f"You're gaining {increment} coin each second")
incrementLabel.pack()

root.mainloop()

