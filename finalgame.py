import pygame, simpleGE

#game dictionary
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

#constants
currentKey = "start"
pathGame = getGame()
currentNode = pathGame[currentKey]
(description, menuA, choiceA, menuB, choiceB) = currentNode

#game
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.display = pygame.display.set_mode((1280, 720), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.setCaption("Adventure Game")

        self.lblOut = simpleGE.Label()
        self.lblOut.center = (640, 400)
        self.lblOut.size = (300, 30)
        self.lblOut.text = "What will you do? 1/2"
        self.lblOut.bgColor = "purple"

        self.txtName = simpleGE.TxtInput()
        self.txtName.center = (640, 550)
        self.txtName.text = ""

        self.btnClickMe = simpleGE.Button()
        self.btnClickMe.center = (640, 600)
        self.btnClickMe.text = "Click me"
            
        self.sprites = [self.lblOut, 
                        self.txtName,
                        self.btnClickMe]
                      
    def processEvent(self, event):
        self.txtName.readKeys(event)

    def process(self):
        if self.btnClickMe.clicked:
            self.btnClickMe.bgColor = "purple" #for testing purposes
            choice = self.txtName.text
            if choice == "1":
                nextKey = choiceA
            elif choice == "2":
                nextKey = choiceB
            else:
                nextKey = currentKey
            return nextKey
        
        keepGoing = True
        while keepGoing:
            if currentKey == ("start"):
                self.questionStart = simpleGE.MultiLabel()
                self.questionStart.center = (640, 250)
                self.questionStart.size = (800, 300)
                self.questionStart.bgColor = "white"
                self.questionStart.textLines = [
                    "When you reach the marked spot, ",
                    "all you see is an old, ",
                    "forked dirt road.",
                    "1. Go left",
                    "2. Go right"
                ]
                self.sprites = [self.questionStart]
            if currentKey == ("left"):
                self.questionLeft = simpleGE.MultiLabel()
                self.questionLeft.center = (640, 250)
                self.questionLeft.size = (800, 300)
                self.questionLeft.bgColor = "white"
                self.questionLeft.textLines = [
                    "As you stroll, you trip over ",
                    "a rock jutting out of the path.",
                    "1. Grab the rock and stow it in your pack",
                    "2. Throw the rock as hard as you can"
                ]
                self.sprites = [self.questionLeft]
            if currentKey == ("right"):
                self.questionRight = simpleGE.MultiLabel()
                self.questionRight.center = (640, 250)
                self.questionRight.size = (800, 300)
                self.questionRight.bgColor = "white"
                self.questionRight.textLines = [
                    "In your excitement, you forget ",
                    "what it is you're looking for.",
                    "1. Stop and try to remember",
                    "2. Keep going and hope something ",
                    "jogs your memory"
                ]
                self.sprites = [self.questionRight]
            if currentKey == ("stow"):
                self.questionStow = simpleGE.MultiLabel()
                self.questionStow.center = (640, 250)
                self.questionStow.size = (800, 300)
                self.questionStow.bgColor = "white"
                self.questionStow.textLines = [
                    "The rock heavily weighs down ",
                    "your pack. Your movement speed is ",
                    "decreased tremendously. ",
                    "1. Get rid of the rock ",
                    "2. Keep the rock "
                ]
                self.sprites = [self.questionStow]
            if currentKey == ("drop"):
                self.questionDrop = simpleGE.MultiLabel()
                self.questionDrop.center = (640, 250)
                self.questionDrop.size = (800, 300)
                self.questionDrop.bgColor = "white"
                self.questionDrop.textLines = [
                    "Before you drop the rock, ",
                    "you consider throwing it. ",
                    "It doesn't take you very ",
                    "long to decide...",
                    "1. Throw the rock ",
                    "2. Start over "
                ]
                self.sprites = [self.questionDrop]
            if currentKey == ("keep"):
                self.questionKeep = simpleGE.MultiLabel()
                self.questionKeep.center = (640, 250)
                self.questionKeep.size = (800, 300)
                self.questionKeep.bgColor = "white"
                self.questionKeep.textLines = [
                    "You keep the rock in your pack. ",
                    "As you keep walking, you realize that "
                    "this rock is prime for throwing, ",
                    "but not for walking with. ",
                    "1. Throw the rock",
                    "2. Start over"
                ]
                self.sprites = [self.questionKeep]
            if currentKey == ("throw"):
                self.questionThrow = simpleGE.MultiLabel()
                self.questionThrow.center = (640, 250)
                self.questionThrow.size = (800, 300)
                self.questionThrow.bgColor = "white"
                self.questionThrow.textLines = [
                    "You muster up all of your strength ",
                    "and throw the rock as hard as you can ",
                    "in front of you. It goes quite the ",
                    "distance before you hear a loud ",
                    "'ouch!'. You hit someone. ",
                    "1. Make it right",
                    "2. Pretend it never happened"
                ]
                self.sprites = [self.questionThrow]
            if currentKey == ("remember"):
                self.questionRem = simpleGE.MultiLabel()
                self.questionRem.center = (640, 250)
                self.questionRem.size = (800, 300)
                self.questionRem.bgColor = "white"
                self.questionRem.textLines = [
                    "After a short rest, you remember: ",
                    "the so-called ancient relic is ",
                    "Elmunster's favorite cheese. Wizards ",
                    "love cheese. What kind of cheese ",
                    "was it again?",
                    "1. It was gouda cheese",
                    "2. It was bleu cheese"
                ]
                self.sprites = [self.questionRem]
            if currentKey == ("onward"):
                self.questionOnward = simpleGE.MultiLabel()
                self.questionOnward.center = (640, 250)
                self.questionOnward.size = (800, 300)
                self.questionOnward.bgColor = "white"
                self.questionOnward.textLines = [
                    "You continue down the path ",
                    "but nothing jogs your memory. ",
                    "Ironically enough, this path is ", 
                    "a dead end. You failed. Return to ",
                    "Elmunster's tower for punishment. ",
                    "1. Start over",
                    "2. Quit"
                ]
                self.sprites = [self.questionOnward]
            if currentKey == ("follow"):
                self.questionFollow = simpleGE.MultiLabel()
                self.questionFollow.center = (640, 250)
                self.questionFollow.size = (800, 300)
                self.questionFollow.bgColor = "white"
                self.questionFollow.textLines = [
                    "You follow the sound and make ",
                    "your way to where the rock landed. ",
                    "There's nobody there, but there is a note. ",
                    "It simply reads: 'I know who you are, ",
                    "and you're not getting any cheese.' You must ",
                    "have hit the local cheesemonger with the rock. ",
                    "1. Go tell Elmunster",
                    "2. Follow the scent of cheese and ",
                    "beg the cheesemonger for forgiveness "
                ]
                self.sprites = [self.questionFollow]
            if currentKey == ("tower"):
                self.questionTower = simpleGE.MultiLabel()
                self.questionTower.center = (640, 250)
                self.questionTower.size = (800, 300)
                self.questionTower.bgColor = "white"
                self.questionTower.textLines = [
                    "Elmunster is extremely angry at you. ",
                    "He smites you before you can say 'cheese'. ",
                    "You failed. ",
                    "1. Start over",
                    "2. Quit"
                ]
                self.sprites = [self.questionTower]
            if currentKey == ("scent"):
                self.questionScent = simpleGE.MultiLabel()
                self.questionScent.center = (640, 250)
                self.questionScent.size = (800, 300)
                self.questionScent.bgColor = "white"
                self.questionScent.textLines = [
                    "The scent leads you left, ",
                    "then right, then left again. ",
                    "After a while, you realize you ",
                    "have been walking in circles.",
                    "1. Start over",
                    "2. Quit"
                ]
                self.sprites = [self.questionScent]
            if currentKey == ("pretend"):
                self.questionPretend = simpleGE.MultiLabel()
                self.questionPretend.center = (640, 250)
                self.questionPretend.size = (800, 300)
                self.questionPretend.bgColor = "white"
                self.questionPretend.textLines = [
                    "As you traverse the dirt path, ",
                    "you see a figure speed-walking in ",
                    "your direction. He smells distinctly ",
                    "of cheese, but you can't make out ",
                    "what kind. He has a rock in his ",
                    "hand. While you're busy thinking about ",
                    "what kind of cheese he smells of, ",
                    "the cheese man throws the rock back at you ",
                    "with such force that you fly all the way ",
                    "back to the beginning of the path. ",
                    "1. Start over",
                    "2. Quit"
                ]
                self.sprites = [self.questionPretend]
            if currentKey == ("gouda"):
                self.questionGouda = simpleGE.MultiLabel()
                self.questionGouda.center = (640, 250)
                self.questionGouda.size = (800, 300)
                self.questionGouda.bgColor = "white"
                self.questionGouda.textLines = [
                    "That's right, it was gouda cheese. ",
                    "That's the wizard's absolute favorite. ",
                    "Now that you remember, you know ",
                    "exactly where to go from here. ",
                    "1. Go to the cheesemonger",
                    "2. Go to the farmer's market"
                ]
                self.sprites = [self.questionGouda]
            if currentKey == ("bleu"):
                self.questionBleu = simpleGE.MultiLabel()
                self.questionBleu.center = (640, 250)
                self.questionBleu.size = (800, 300)
                self.questionBleu.bgColor = "white"
                self.questionBleu.textLines = [
                    "You think it was bleu cheese, ",
                    "extra mouldy. You know exactly ",
                    "where to go from here. ",
                    "1. Go to the cheesemonger",
                    "2. Go to the farmer's market"
                ]
                self.sprites = [self.questionBleu]
            if currentKey == ("go"):
                self.questionGo = simpleGE.MultiLabel()
                self.questionGo.center = (640, 250)
                self.questionGo.size = (800, 300)
                self.questionGo.bgColor = "white"
                self.questionGo.textLines = [
                    "Once you reach the cheesemonger's ",
                    "you proudly purchase the gouda cheese. ",
                    "The cheesemonger thanks you for your purchase ",
                    "and wishes you a nice day. ",
                    "With trembling hands, you kneel before Elmunster ",
                    "and present the gouda. He cries tears of joy ",
                    "and eats it right away. You win! ",
                    "1. Start over",
                    "2. Quit"
                ]
                self.sprites = [self.questionGo]
            if currentKey == ("farmer"):
                self.questionFarmer = simpleGE.MultiLabel()
                self.questionFarmer.center = (640, 250)
                self.questionFarmer.size = (800, 300)
                self.questionFarmer.bgColor = "white"
                self.questionFarmer.textLines = [
                    "You make your way to the farmer's ",
                    "market, but you don't see any cheese. ",
                    "You failed. ",
                    "1. Start over",
                    "2. Quit"
                ]
                self.sprites = [self.questionFarmer]
            if currentKey == ("goBleu"):
                self.questiongoBleu = simpleGE.MultiLabel()
                self.questiongoBleu.center = (640, 250)
                self.questiongoBleu.size = (800, 300)
                self.questiongoBleu.bgColor = "white"
                self.questiongoBleu.textLines = [
                    "Once you reach the cheesemonger's ",
                    "stand, you proudly purchase the bleu cheese. ",
                    "You can tell by the look on his face that he is ",
                    "judging you. Back at the tower, you hesitantly ",
                    "kneel before Elmunster to present the mouldy cheese... ",
                    "but before you can explain yourself, he casts fireball ",
                    "and aims it directly at you. Should you survive, ",
                    "you are banished from the realm forever.",
                    "1. Start over",
                    "2. Quit"
                ]
                self.sprites = [self.questiongoBleu]
            if currentKey == ("quit"):
                keepGoing = False

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
