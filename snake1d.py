from game1d import Game1d
from random import randrange

class Snake(Game1d):
    def gameInit(self):
        self.player = randrange(256)
        self.tail = []
        self.fruit = randrange(256)

    def draw(self,buttons,display):
        display = [(0,0,0) for i in range(len(display))] #clear entire display
        if(buttons['R']):
            self.tail.append(self.player)
            self.tail.pop(0)
            self.player +=1
        if(buttons['L']):
            self.tail.append(self.player)
            self.tail.pop(0)
            self.player -=1

        self.player = self.player % len(display) #wrap around

        if(self.player==self.fruit):
            
            self.fruit = randrange(256)
            self.tail.insert(0,self.player)


        display[self.player] = (125,0,125)
        for i in range(len(self.tail)):
            mod = 120 - (10*i) #fade tail out
            if mod <10:
                mod = 10
            display[self.tail[len(self.tail) -i - 1]] = (mod,0,mod)
        display[self.fruit] = (0,125,0)
        return display
