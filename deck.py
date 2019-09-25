import random

nigiriArray = ["Egg Nigiri", "Salmon Nigiri", "Squid Nigiri"]
rollsArray = ["Maki", "Temaki", "Uramaki"]
appetizerArray = ["Tempura", "Sashimi", "Dumpling", "Eel", "Tofu", "Onigiri", "Edamame", "Miso Soup"]
specialArray = ["Chopsticks", "Soy Sauce", "Tea", "Menu", "Spoon", "Special Order", "Takeout Box", "Wasabi"]
dessertArray = ["Pudding", "Green Tea Ice Cream", "Fruit"]
parentArray = [nigiriArray, rollsArray, appetizerArray, specialArray, dessertArray]

makiCountArray = [1,1,1,1,2,2,2,2,2,3,3,3]
uramakiCountArray = [3,3,3,3,4,4,4,4,5,5,5,5]
temakiCountArray = [1]
rollCountArray = [makiCountArray, temakiCountArray, uramakiCountArray]

#0 = box, 1 = sandwich, 2 = anime donut, 3 = roll
onigiriTypeArray = [0, 0, 1, 1, 2, 2, 3, 3]

#fruit description: each digit is either watermelon, pineapple, or orange
fruitCountArray = [200, 200, 200, 020, 020, 020, 002, 002, 002, 110, 110, 011, 011, 101, 101]
numberOfNigiri = 12

numberOfSushiRolls = 12
numberOfAppetizers = 8
numberOfSpecials = 3
numberOfFirstDesserts = 5
class Deck:

    def __init__(self, rollIndex, appetizerIndices, specialIndices, dessertIndex):
        if (self.resetDeck(rollIndex, appetizerIndices, specialIndices, dessertIndex) == 0):
            return 0
        
    def dealCards(self, numberOfCards):
        hand = []
        for i in range(numberOfCards):
            hand.append(self.deck.pop(0))
        return hand

    def returnCards(self, leftoverCards):
        self.deck = self.deck + leftoverCards
        

    def resetDeck(self, rollIndex, appetizerIndices, specialIndices, dessertIndex):
        if (len(appetizerIndices) != 3):
            return 0
        if (len(specialIndices) != 2):
            return 0
        
        self.rollType = rollIndex
        
        self.appetizerOne = appetizerIndices[0]
        self.appetizerTwo = appetizerIndices[1]
        self.appetizerThree = appetizerIndices[2]
        
        self.specialOne = specialIndices[0]
        self.specialTwo = specialIndices[1]
        
        self.dessertType = dessertIndex
        
        self.deck = []
        
        #four egg nigiri
        #five salmon nigiri
        #three squid nigiri
        self.deck = self.deck + [0,0,0,0,1,1,1,1,1,2,2,2]
        
        for i in range(numberOfSushiRolls):
			if (rollIndex == 1): # temaki don't have varying amounts
				self.deck.append(110)
			else:
				self.deck.append(100 + 10 * rollIndex + i)
        
        for i in range(numberOfAppetizers):
            self.deck.append(200 + self.appetizerOne * 10)
            self.deck.append(200 + self.appetizerTwo * 10)
            self.deck.append(200 + self.appetizerThree * 10)
        
        for i in range(numberOfSpecials):
            self.deck.append(300 + self.specialOne * 10)
            self.deck.append(300 + self.specialTwo * 10)
        
        for i in range(numberOfFirstDesserts):
            self.deck.append(400 + self.dessertType * 10)
        
        random.shuffle(self.deck)
def printHand(hand):
    string = ""
    for card in hand:
        string = string + parentArray[get_cardType(card)][get_cardTypeIndex(card)] + ", "
    print(string)
def get_cardType(value):
    return int(value / 100)
    
def get_cardTypeIndex(value):
    return int((value % 100) / 10)

def get_cardSubIndex(value):
	return value % 10
