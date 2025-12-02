import pygame, simpleGE

def getGame(): 
    pathGame = {
        "start": ["When you reach the marked spot, all you see is an old, forked dirt road.", "1. Go left", "left", "2. Go right", "right"],
        "left": ["As you stroll, you trip over a rock jutting out of the path.", "1. Grab the rock and stow it in your pack", "stow", "2. Throw the rock as hard as you can", "throw"],
        "right": ["In your excitement, you forget what it is you're looking for.", "1. Stop and try to remember", "remember", "2. Keep going and hope something jogs your memory", "onward"],
        "stow": ["The rock heavily weighs down your pack. You movement speed is slowed down tremendously.", "1. Get rid of the rock", "drop", "2. Keep the rock and deal with the slowness", "keep"],
        "drop": ["Before you drop the rock, you consider throwing it. It doesn't take you very long to decide.", "1. Throw the rock", "throw", "2. Start over", "start"],
        "keep": ["You keep the rock in your pack. As you keep walking, you realize that this rock is prime for throwing, but not for walking with.", "1. Throw the rock", "throw", "2. Start over", "start"],
        "throw": ["You muster up all of your strength and throw the rock as hard as you can in front of you. It goes quite the distance before you hear a loud 'ouch!'. You hit someone.", "1. Make it right.", "follow", "2. Pretend it never happened", "pretend"],
        "remember": ["After a short rest, you remember: the so-called ancient relic is Elmunster's favorite cheese. Wizards love cheese. What kind of cheese was it again?", "1. It was gouda cheese", "gouda", "2. It was bleu cheese", "bleu"],
        "onward": ["You continue down the path, but nothing jogs your memory. Ironically enough, this path is a dead end. You have failed. Return to Elmunster's tower for punishment.", "1. Start over", "start", "2. Quit", "quit"],
        "follow": ["You follow the sound and make your way to where the rock landed. There's nobody there, but there is a note. It simply reads: 'I know who you are, and you're not getting any of my cheese.' That's funny, because cheese is the ancient relic Elmunster sent you to grab. You must have hit the cheesemonger with the rock. Awkward...", "1. Go back to Elmunster's tower and tell him the unfortunate news", "tower", "2. Follow the scent of cheese and beg the cheesemonger for forgiveness", "scent"],
        "tower": ["Elmunster is extremely angry at you. He smites you before you can say 'cheese'. You failed.", "1. Start over", "start", "2. Quit", "quit"],
        "scent": ["The scent leads you left, then right, then left again. After a while, you realize you have been walking in circles. Whoops.", "1. Start over", "start", "2. Quit", "quit"],
        "pretend": ["As you traverse the dirt path, you see a figure speed-walking in your direction. He smells distinctly of cheese, but you can't make out what kind. He has a rock in his hand. While you're busy thinking about what kind of cheese he smells of, the cheese man throws the rock back at you with such force that you fly all the way back to the beginning of the path.", "1. Start over", "start", "2. Quit", "quit"],
        "gouda": ["That's right, it was gouda cheese. That's the wizard's absolute favorite. Now that you remember, you know exactly where to go from here.", "1. Go to the cheesemonger", "go", "2. Go to the farmer's market", "farmer"],
        "bleu": ["You think it was bleu cheese, extra mouldy. You know exactly where to go from here.", "1. Go to the cheesemonger", "goBleu", "2. Go to the farmer's market", "farmer"],
        "go": ["Once you reach the cheesemonger's stand, you proudly purchase the gouda cheese. The cheesemonger thanks you for your purchase and wishes you a nice day. It is dark once you make it back to Elmunster's tower. With trembling hands, you kneel before him and present the gouda. The old wizard cries tears of joy and eats it right away. Congratulations - you win.", "1. Start over", "start", "2. Quit", "quit"],
        "farmer": ["You make your way to the farmer's market, but you don't see any cheese - definitely not the kind that you're looking for, anyway. That was your only lead. You have failed.", "1. Start over", "start", "2. Quit", "quit"],
        "goBleu": ["Once you reach the cheesemonger's stand, you proudly purchase the bleu cheese. You can tell by the look on his face that the cheesemonger is judging you for your choice of cheese. Back at the tower, you hesitantly kneel before Elmunster to present the mouldy cheese... but before you can explain yourself, Elmunster casts fireball and aims it directly at you. That was the wrong cheese. Should you survive the fireball, you will be banished from the realm.", "1. Start over", "start", "2. Quit", "quit"]
        }
    return pathGame

currentKey = "start"
pathGame = getGame()
currentNode = pathGame[currentKey]
(description, menuA, choiceA, menuB, choiceB) = currentNode

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()

        self.output = simpleGE.MultiLabel()
        self.output.center = (320, 250)
        self.output.size = (800, 300)
        self.output.textLines = [
                description,
                menuA,
                menuB]
        self.output.font.size = 12
        
        self.lblOut = simpleGE.Label()
        self.lblOut.center = (320, 100)
        self.lblOut.size = (300, 30)
        self.lblOut.text = f"What will you do? 1/2"

        self.txtName = simpleGE.TxtInput()
        self.txtName.center = (320, 200)
        self.txtName.text = ""

        self.btnClickMe = simpleGE.Button()
        self.btnClickMe.center = (320, 300)
        self.btnClickMe.text = "Click me"

        self.sprites = [self.output,
                        self.lblOut, 
                        self.txtName,
                        self.btnClickMe]
        
    def processEvent(self, event):
        self.txtName.readKeys(event)

    def process(self):
        if self.btnClickMe.clicked:
            keepGoing = True
            while keepGoing:
                if currentKey == "quit":
                    keepGoing = False
                else:
                    choice = self.txtName.text
                    if choice == 1:
                        nextKey = choiceA
                    if choice == 2:
                        nextKey = choiceB
                    else:
                        nextKey == currentKey
                    return nextKey

        if currentKey == "start":
            self.setImage("fork.png")
        if currentKey == "left":
            self.setImage("rock.png")
        if currentKey == "right":
            self.setImage("forgot.png")
        if currentKey == "stow":
            self.setImage("slow.png")
        if currentKey == "drop":
            self.setImage("rock.png")
        if currentKey == "keep":
            self.setImage("rock.png")
        if currentKey == "throw":
            self.setImage("throw.png")
        if currentKey == "remember":
            self.setImage("bulb.png")
        if currentKey == "onward":
            self.setImage("elmunsterstower.png")
        if currentKey == "follow":
            self.setImage("note.png")
        if currentKey == "tower":
            self.setImage("elmunsterstower.png")
        if currentKey == "scent":
            self.setImage("rock.png")
        if currentKey == "gouda":
            self.setImage("cheese.png")
        if currentKey == "bleu":
            self.setImage("cheese.png")
        if currentKey == "go":
            self.setImage("stand.png")
        if currentKey == "farmer":
            self.setImage("stand")
        if currentKey == "goBleu":
            self.setImage("elmunsterstower.png")
    
def main():
    game = Game()
    game.start()
    
  
if __name__ == "__main__":
    main()
