import time

class Game:
    def __init__(self):
        self.coins = 10
        self.coinFactoryQuantity = 0
        self.coinFactoryCost = 10
        self.incrementUpgrades = 1
        self.speed = 1
        self.startTime = time.time()

        self.upgradeList = {
            "timeElapsedUp": False
        }

        self.upgradeCostsList = {
            "timeElapsedUp": 50
        }

    def getIncrement(self):
        self.increment = self.coinFactoryQuantity * self.incrementUpgrades * 0.001 * self.speed
        return self.increment

    def coinIncrement(self):
        self.increment = self.getIncrement()
        self.coins += self.increment
    
    def tryBuy(self, target, cost):
        if (self.coins - cost < 0):
            return False
        match target:
            case "CFQ":
                self.coinFactoryQuantity += 1
                self.coinFactoryCost *= 2
            case "TEU":
                if (not self.upgradeList["timeElapsedUp"]):
                    self.upgradeList["timeElapsedUp"] = True
                    self.upgradesUpdate()
                else:
                    return False
        self.coins -= cost
        return True
                
    def upgradesUpdate(self):
        teu = 1
        if(self.upgradeList["timeElapsedUp"]):
            currentTime = time.time()
            teu = max((currentTime - self.startTime) * 0.1, 1)
        self.incrementUpgrades = teu