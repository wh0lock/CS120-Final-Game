import pygame, simpleGE

def getGame(): 
    pathGame = {
        "start": ["You are a brand new adventurer. Elmunster, the local wizard, has tasked you with finding an ancient relic, but all he has given you in aid is a map. When you reach the marked spot, all you see is an old, forked dirt road.", "Go left", "left", "Go right", "right"],
        "left": ["As you stroll, you trip over a rock jutting out of the path.", "Grab the rock and stow it in your pack", "stow", "Throw the rock as hard as you can", "throw"],
        "right": ["In your excitement, you forget what it is you're looking for.", "Stop and try to remember", "remember", "Keep going and hope something jogs your memory", "onward"],
        "stow": ["The rock heavily weighs down your pack. You movement speed is slowed down tremendously.", "Get rid of the rock", "drop", "Keep the rock and deal with the slowness", "keep"],
        "drop": ["Before you drop the rock, you consider throwing it. It doesn't take you very long to decide.", "Throw the rock", "throw", "Start over", "start"],
        "keep": ["You keep the rock in your pack. As you keep walking, you realize that this rock is prime for throwing, but not for walking with.", "Throw the rock", "throw", "Start over", "start"],
        "throw": ["You muster up all of your strength and throw the rock as hard as you can in front of you. It goes quite the distance before you hear a loud 'ouch!'. You hit someone. Are you going to make it right, or pretend it never happened and hope you don't run into them further down the path?", "Make it right. Follow the screaming and apologize to whoever you hit.", "follow", "Pretend it never happened. What are the chances you run into this person anyway? You've got a job to do.", "pretend"],
        "remember": ["After a short rest, you remember: the so-called ancient relic is Elmunster's favorite cheese. Wizards love cheese. What kind of cheese was it again?", "It was gouda cheese", "gouda", "It was bleu cheese", "bleu"],
        "onward": ["You continue down the path, but nothing jogs your memory. Ironically enough, this path is a dead end. You have failed. Return to Elmunster's tower for punishment.", "Start over", "start", "Quit", "quit"],
        "follow": ["You follow the sound and make your way to where the rock landed. There's nobody there, but there is a note. It simply reads: 'I know who you are, and you're not getting any of my cheese.' That's funny, because cheese is the ancient relic Elmunster sent you to grab. You must have hit the cheesemonger with the rock. Awkward...", "Go back to Elmunster's tower and tell him the unfortunate news", "tower", "Follow the scent of cheese and beg the cheesemonger for forgiveness", "scent"],
        "tower": ["Elmunster is extremely angry at you. He smites you before you can say 'cheese'. You failed.", "Start over", "start", "Quit", "quit"],
        "scent": ["The scent leads you left, then right, then left again. After a while, you realize you have been walking in circles. Whoops.", "Start over", "start", "Quit", "quit"],
        "pretend": ["As you traverse the dirt path, you see a figure speed-walking in your direction. He smells distinctly of cheese, but you can't make out what kind. He has a rock in his hand. While you're busy thinking about what kind of cheese he smells of, the cheese man throws the rock back at you with such force that you fly all the way back to the beginning of the path.", "Start over", "start", "Quit", "quit"],
        "gouda": ["That's right, it was gouda cheese. That's the wizard's absolute favorite. Now that you remember, you know exactly where to go from here.", "Go to the cheesemonger", "go", "Go to the farmer's market", "farmer"],
        "bleu": ["You think it was bleu cheese, extra mouldy. You know exactly where to go from here.", "Go to the cheesemonger", "goBleu", "Go to the farmer's market", "farmer"],
        "go": ["Once you reach the cheesemonger's stand, you proudly purchase the gouda cheese. The cheesemonger thanks you for your purchase and wishes you a nice day. It is dark once you make it back to Elmunster's tower. With trembling hands, you kneel before him and present the gouda. The old wizard cries tears of joy and eats it right away. Congratulations - you win.", "Start over", "start", "Quit", "quit"],
        "farmer": ["You make your way to the farmer's market, but you don't see any cheese - definitely not the kind that you're looking for, anyway. That was your only lead. You have failed.", "Start over", "start", "Quit", "quit"],
        "goBleu": ["Once you reach the cheesemonger's stand, you proudly purchase the bleu cheese. You can tell by the look on his face that the cheesemonger is judging you for your choice of cheese. Back at the tower, you hesitantly kneel before Elmunster to present the mouldy cheese... but before you can explain yourself, Elmunster casts fireball and aims it directly at you. That was the wrong cheese. Should you survive the fireball, you will be banished from the realm.", "Start over", "start", "Quit", "quit"]
        }
    return pathGame

def playNode(pathGame, currentKey):
    currentNode = pathGame[currentKey]
    (description, menuA, choiceA, menuB, choiceB) = currentNode
    print(f"""
          {description}
          1) {menuA}
          2) {menuB}
        """)
    choice = input("What will you do? 1/2: ")
    if choice == "1":
        nextKey = choiceA
    if choice == "2":
        nextKey = choiceB
    else:
        nextKey == currentKey
    return nextKey

class Begin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "start":
            self.setImage("fork.png")

class Left(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "left":
            self.setImage("rock.png")

class Right(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "right":
            self.setImage("forgot.png")

class Stow(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "stow":
            self.setImage("slow.png")

class Drop(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "drop":
            self.setImage("rock.png")

class Keep(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "keep":
            self.setImage("rock.png")

class Throw(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "keep":
            self.setImage("throw.png")

class Remember(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "remember":
            self.setImage("bulb.png")

class Onward(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "onward":
            self.setImage("elmunsterstower.png")

class Follow(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "follow":
            self.setImage("note.png")

class Tower(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "follow":
            self.setImage("elmunsterstower.png")

class Scent(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "scent":
            self.setImage("circle.png")

class Pretend(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "scent":
            self.setImage("rock.png")

class Gouda(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "gouda":
            self.setImage("cheese.png")

class Bleu(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "bleu":
            self.setImage("cheese.png")

class Go(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "go":
            self.setImage("stand")

class Farmer(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "farmer":
            self.setImage("stand")

class GoBleu(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        pathGame = getGame()
        currentKey = playNode(pathGame, currentKey)
        if currentKey == "goBleu":
            self.setImage("elmunsterstower.png")

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        pathGame = getGame()
        currentKey = "start"
        keepGoing = True
        while keepGoing:
            if currentKey == "quit":
                keepGoing = False
            else:
                currentKey = playNode(pathGame, currentKey)
        
        self.begin = Begin(self)
        self.left = Left(self)
        self.right = Right(self)
        self.stow = Stow(self)
        self.drop = Drop(self)
        self.keep = Keep(self)
        self.throw = Throw(self)
        self.remember = Remember(self)
        self.onward = Onward(self)
        self.follow = Follow(self)
        self.tower = Tower(self)
        self.scent = Scent(self)
        self.pretend = Pretend(self)
        self.gouda = Gouda(self)
        self.bleu = Bleu(self)
        self.go = Go(self)
        self.farmer = Farmer(self)
        self.goBleu = GoBleu(self)

        
        self.sprites = [self.begin,
                        self.left,
                        self.right,
                        self.stow,
                        self.drop,
                        self.keep,
                        self.throw,
                        self.remember,
                        self.onward,
                        self.follow,
                        self.tower,
                        self.scent,
                        self.pretend,
                        self.gouda,
                        self.bleu,
                        self.go,
                        self.farmer,
                        self.goBleu]
        
def main(): 
    game = Game()
    game.start()
        
if __name__ == "__main__":
    main()
