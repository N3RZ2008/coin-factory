class Game:
    def __init__(self):
        self.coins = 10
        self.coinFactoryQuantity = 0
        self.coinFactoryCost = 10
        self.upgrades = 1
        self.speed = 1

    def getIncrement(self):
        self.increment = self.coinFactoryQuantity * self.upgrades * 0.001 * self.speed
        return self.increment

    def coinIncrement(self):
        self.increment = self.getIncrement()
        self.coins += self.increment
    
    def tryBuy(self, target, cost):
        if (self.coins - cost < 0):
            return False
        self.coins -= cost
        match target:
            case "CFQ":
                self.coinFactoryQuantity += 1
                self.coinFactoryCost *= 2
        return True
                
         