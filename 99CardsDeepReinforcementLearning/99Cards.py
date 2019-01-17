import random

#a simple version of the game 99Cards
class Board:
    def __init__(self, seed = 0):
        if seed != 0: random.seed(seed)
        cards = [i for i in range(2,100)]
        random.shuffle(cards)
        self.state = [1, 1, 100,100]+cards
        self.observable = self.state[0:12]
        self.cardsRemaining = 99
        self.score = 0
        
    def playAction(self, stack, card):
        cardIndex = card+4
        
        if(self.isValidAction(stack, card)):
            self.state[stack] = self.state[cardIndex]
            self.state = self.state[0:cardIndex] + self.state[cardIndex+1:]+[0]
            self.observable = self.state[0:12]
                
            self.score += 99-self.cardsRemaining
            self.cardsRemaining = self.cardsRemaining - 1
            
            return (99.0-(self.cardsRemaining+1))
        else:
            return -1000
        
        
    def isValidAction(self, stack, card):
        if stack < 0  or stack > 3:
            return False
        if card < 0 or card > 7:
            return False
        
        cardIndex = card+4
        if self.state[cardIndex] == 0: return False
        
        diff = abs(self.state[stack]-self.state[cardIndex])
        
        if(stack < 2):
            return self.state[stack] < self.state[cardIndex] or diff == 10
        else:
            return self.state[stack] > self.state[cardIndex] or diff == 10
        
    def getActionList(self):
        result = []
        for stack in range(4):
            for card in range(0, 7):
                result.append((stack,card))
        return list(filter(lambda x: self.isValidAction(x[0],x[1]), result))


#this function is useless except if you want to play the game with no GUI for all intents and purposes
def play(seed):
    board = Board(seed)
    while(len(board.getActionList()) > 0 or board.cardsRemaining != 0):
        
        card = raw_input("which card")
        stack = raw_input("which stack")
        
        if board.isValidAction(stack, card):
            board.playAction(stack,card)
            
    return board.score
        
    
