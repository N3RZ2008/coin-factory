import tkinter as tk
from tkinter import ttk

class Screen:
    def __init__(self, root, game):
        self.root = root
        self.game = game

        self.root.title("CoinFactory")
        self.root.geometry("600x600")

        self.coinsLabel = ttk.Label(root, text=self.game.coins)
        self.coinsLabel.pack()
        self.incrementLabel = ttk.Label(root, text=f"You're gaining {self.game.getIncrement()} coin each second")
        self.incrementLabel.pack()
        self.coinFactoryButton = ttk.Button(root, text=f"Buy Coin Factory ({self.game.coinFactoryCost} coins)", command=lambda: self.tryBuy("CFQ", self.game.coinFactoryCost))
        self.coinFactoryButton.pack()
        self.timeElapsedUp = ttk.Button(root, text= f"Multiplier based on time elapsed ({self.game.upgradeCostsList["timeElapsedUp"]} coins)", command=lambda: self.tryBuy("TEU", self.game.upgradeCostsList["timeElapsedUp"]))
        self.timeElapsedUp.pack()
        # debugButton = ttk.Button(root, text= "Debug", command=self.debug).pack()

    def updateScreen(self):
        self.coinsLabel.config(text=f'{self.game.coins:.2f}')
        self.coinFactoryButton.config(text=f"Buy Coin Factory ({self.game.coinFactoryCost} coins)")
        self.incrementLabel.config(text=f"You're gaining {self.game.increment * 1000:.2f} coin each second")
        if (self.game.upgradeList["timeElapsedUp"]):
            self.timeElapsedUp.config(text="Multiplier based on time elapsed (Bought)")
    
    def schedule(self):
        self.game.upgradesUpdate()
        self.game.coinIncrement()
        self.updateScreen()
        self.root.after(1, self.schedule)
    
    def tryBuy(self, target, cost):
        if (self.game.tryBuy(target, cost)):
            self.updateScreen()
    
    def debug(self):
        print(self.game.getIncrement())
    