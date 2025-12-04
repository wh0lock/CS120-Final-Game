# Emily Adams
# 12/04/2025
# CS120 Final Game: "Elmunster's Quest"
# User's choices decide if they successfully complete the quest... or not. Good luck!

import pygame, simpleGE

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.nodes = {}
        self.setCaption("Elmunster's Quest")

        self.getGame()

        self.backgroundMusic = simpleGE.Sound("Woodland Fantasy.mp3")
        self.backgroundMusic.play()
        self.setImage("use8948-5.png")

        pygame.font.init()

        self.lblDescription = simpleGE.MultiLabel()
        self.lblDescription.textLines = [
            "",
            "",
            "",
            "",
            ""
        ]
        self.lblDescription.center = (320, 150)
        self.lblDescription.size = (640, 320)
        self.lblDescription.bgColor = "darkslategray"
        self.lblDescription.font = pygame.font.Font("Metamorphous-Regular.ttf", 20)
        self.lblDescription.font.set_bold(True)

        self.buttonA = simpleGE.Button()
        self.buttonA.text = "choice A"
        self.buttonA.center = (150, 400)
        self.buttonA.size = (250, 40)
        self.buttonA.font = pygame.font.Font("Metamorphous-Regular.ttf", 20)
        self.buttonA.font.set_bold(True)

        self.buttonB = simpleGE.Button()
        self.buttonB.text = "choice B"
        self.buttonB.center = (500, 400)
        self.buttonB.size = (250, 40)
        self.buttonB.font = pygame.font.Font("Metamorphous-Regular.ttf", 20)
        self.buttonB.font.set_bold(True)
            
        self.sprites = [self.lblDescription,
                        self.buttonA, 
                        self.buttonB]
        
        self.currentKey = "start"
        self.displayNode(self.currentKey)

    def getGame(self): 
        self.nodes = {
        "start": [["When you reach the", "marked spot Elmunster showed you,", "all you see is an old, forked dirt road."], "Go left", "left", "Go right", "right"],
        "left": [["As you stroll, you trip", "over a rock jutting out of the path."], "Stow the rock", "stow", "Throw the rock", "throw"],
        "right": [["In your excitement, you", "forget what it is ", "you're looking for."], "Try to remember", "remember", "Wing it", "onward"],
        "stow": [["The rock heavily weighs", "down your pack. Your ", "movement speed is slowed", "down tremendously."], "Drop the rock", "drop", "Keep the rock", "keep"],
        "drop": [["Before you drop the rock, ", "you consider throwing it.", "It doesn't take you", "very long to decide."], "Throw the rock", "throw", "Start over", "start"],
        "keep": [["You keep the rock in", "your pack. As you keep walking,", "you realize that this rock", "is prime for throwing, ", "but not for walking with."], "Throw the rock", "throw", "Start over", "start"],
        "throw": [["You muster up all of", "your strength and throw", "the rock as hard as", "you can in front of you. It", "goes quite the distance before", "you hear a loud 'ouch!'. You hit someone."], "Make it right", "follow", "Keep going", "pretend"],
        "remember": [["After a short rest, you remember:", "the so-called ancient relic is", "Elmunster's favorite cheese. Wizards ", "love cheese. What kind of cheese was it again?"], "Gouda", "gouda", "Bleu", "bleu"],
        "onward": [["You continue down the path, ", "but nothing jogs your memory.", "Ironically enough, this path is", "a dead end. You have failed. Return to ", "Elmunster's tower for punishment."], "Start over", "start", "Quit", "quit"],
        "follow": [["You follow the sound and make", "your way to where the rock ", "landed. There's nobody there, but there is a note.", "It simply reads: 'I know who you are, and you're", "not getting any of my cheese.' That's", "funny, because cheese is the ancient relic", "Elmunster sent you to grab. You must have hit the", "cheesemonger with the rock. Awkward..."], "Go tell Elmunster", "tower", "Beg for forgiveness", "scent"],
        "tower": [["Elmunster is extremely angry", "at you. He smites you before you", "can say 'cheese'. You failed."], "Start over", "start", "Quit", "quit"],
        "scent": [["The cheese scent leads you left,", "then right, then left again.", "After a while, you realize", "you have been walking in circles. Whoops."], "Start over", "start", "Quit", "quit"],
        "pretend": [["As you traverse the dirt path, you see", "a figure speed-walking in your direction. He smells", "of cheese, but you can't make out what kind.", "He has a rock in his hand. While you're ", "busy thinking about what kind", "of cheese he smells of, the cheese man", "throws the rock back at you with such", "force that you fly all the way back", "to the beginning of the path."], "Start over", "start", "Quit", "quit"],
        "gouda": [["That's right, it was gouda cheese.", "That's the wizard's absolute favorite.", "Now that you remember, you know", "exactly where to go from here."], "Go to cheesemonger", "go", "Go to farmer's market", "farmer"],
        "bleu": [["You think it was bleu cheese,", "extra mouldy. You know exactly", "where to go from here."], "Go to cheesemonger", "goBleu", "Go to farmer's market", "farmer"],
        "go": [["Once you reach the cheesemonger's stand,", "you proudly purchase the gouda cheese.", "The cheesemonger thanks you for your", "purchase and wishes you a nice day.", "With trembling hands, you kneel before him", "and present the gouda. The old wizard cries", "tears of joy and eats it right away.", "Congratulations - you win."], "Start over", "start", "Quit", "quit"],
        "farmer": [["You make your way to the farmer's market,", "but you don't see any cheese - definitely not", "the kind that you're looking for,", "anyway. That was your only lead. You have failed."], "Start over", "start", "Quit", "quit"],
        "goBleu": [["Once you reach the cheesemonger's stand,", "you proudly purchase the bleu cheese.", "You can tell by the look on his face that the", "cheesemonger is judging you for your choices.", "Back at the tower, you hesitantly kneel before", "Elmunster to present the mouldy cheese... but before you", "can explain yourself, Elmunster casts fireball and aims it", "directly at you. That was the wrong cheese. Should you", "survive the fireball, you will be banished from the realm."], "Start over", "start", "Quit", "quit"]
        }
                      
    def displayNode(self, nodeKey):
        currentNode = self.nodes[nodeKey]
        (description, menuA, nodeA, menuB, nodeB) = currentNode
        self.lblDescription.textLines = description
        self.buttonA.text = menuA
        self.buttonB.text = menuB
        self.nodeA = nodeA
        self.nodeB = nodeB

    def process(self):
        if self.buttonA.clicked:
            if self.nodeA == "quit":
                self.stop()
            else:
                self.displayNode(self.nodeA)

        if self.buttonB.clicked:
            if self.nodeB == "quit":
                self.stop()
            else:
                self.displayNode(self.nodeB)
        
        if self.buttonA.active:
            self.buttonA.bgColor = "saddlebrown"
        else:
            self.buttonA.bgColor = "salmon4"

        if self.buttonB.active:
            self.buttonB.bgColor = "saddlebrown"
        else:
            self.buttonB.bgColor = "salmon4"


def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()

