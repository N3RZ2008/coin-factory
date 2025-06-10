import tkinter as tk

coins = 10
coinFactoryQuantity = 0
coinFactoryCost = 10
upgrades = 1
increment = coinFactoryQuantity * upgrades

def debug():
    print(coinFactoryQuantity)

def updateScreen():
    global coins
    coinsLabel.config(text=coins)
    coinFactoryButton.config(text=f"Buy Coin Factory ({coinFactoryCost} coins)")
    incrementLabel.config(text=f"You're gaining {increment} coin each second")

def coinIncrement():
    global coins
    global increment
    increment = coinFactoryQuantity * upgrades
    coins += increment
    updateScreen()
    root.after(1000, coinIncrement)

def tryBuy(target, cost):
    global coins
    global coinFactoryQuantity
    global coinFactoryCost
    if (coins - cost < 0):
        return False
    coins -= cost
    match target:
        case "CFQ":
            coinFactoryQuantity += 1
            coinFactoryCost *= 2
            updateScreen()
    return True

root = tk.Tk()
root.title("CoinFactory")
root.geometry("600x600")
root.after(1000, coinIncrement)

coinsLabel = tk.Label(root, text=coins)
coinsLabel.pack()
incrementLabel = tk.Label(root, text=f"You're gaining {increment} coin each second")
incrementLabel.pack()
coinFactoryButton = tk.Button(root, text=f"Buy Coin Factory ({coinFactoryCost} coins)", command=lambda: tryBuy("CFQ",coinFactoryCost))
coinFactoryButton.pack()
#debugButton = tk.Button(root, text= "Debug", command=debug).pack()

root.mainloop()

