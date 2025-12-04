# CS120-Final-Game
This is a game in which the user makes their own decisions and their choices decide how the story will end. 
```
Game Design Document
Choose-Your-Own-Adventure (Graphical)

OVERVIEW
The premise is as follows: you are a bright eyed, hopeful adventurer looking for places to be and things to do. A weathered old wizard
sends you on a quest to find an ancient relic, but he doesn't give you very many details to go on; all you have is a place to start.
You go where he marked the map and are met with a fork in the road. What you choose will determine the success of your adventure.

STATE TRANSITION DIAGRAM
Please refer to State Transition Diagram.png.

THE GAME CLASS
Please refer to Game Scene Diagram.png.
Primary class. Subclassed from simpleGE.Scene.
Visual attributes:
    - lblDescription - simpleGE MultiLable
    - buttonA - simpleGE Button
    - buttonB - simpleGE Button

Initializer creates components:
init:
    super init
    self.nodes = {}
    set caption to "Elmunster's Quest"
    
    self.getGame() (calling game function)

    self.backgroundMusic set to "Woodland Fantasy.mp3"
    background music initialized
    image set to "use8948-5.png" (forest scene)

    pygame font initialized

    self.lblDescription made
    self.buttonA made
    self.buttonB made
        all fonts: Metamorphous-Regular.ttf, size 20
    
    sprites: self.lblDescription, self.buttonA, self.buttonB

    self.currentKey = "start"
    self.displayNode(self.currentKey)

define function "getGame(self)"
    writes self.nodes dict

define function "displayNode(self, nodeKey):
    currentNode gets self.nodes[nodeKey]
    currentNode gets (description, menuA, nodeA, menuB, nodeB)
    lblDescription textLines get description
    buttonA text gets menuA
    buttonB text gets menuB
    self.nodeA gets nodeA
    self.nodeB gets nodeB

process(self):
    if buttonA clicked: 
        if self.nodeA is "quit":
            self.stop()
        else:
            self.displayNode(self.nodeA)
    
    if buttonB clicked:
        if self.nodeB is "quit":
            self.stop()
        else:
            self.displayNode(self.nodeB)

    if buttonA is active, make bgColor saddlebrown, else bgColor is salmon4
    if buttonB is active, make bgColor saddlebrown, else bgColor is salmon4

MAIN:
    game = Game() --> calls/inits game class
    game.start() --> starts game

ASSETS:
    backgroundMusic: "Woodland Fantasy" by Matthew Pablo on OpenGameArt.org
    image: "Night forest background" by Olga Bikmullina on OpenGameArt.org
    font: Metamorphous-Regular.ttf, Google Fonts, OFL

PROCESS & REFLECTION:
    This project showed me just how difficult game development is for intermediate programmers. I considered myself decently fluent in Python before taking this class, but now I know that my knowledge is just the tip of the iceberg. To be fair, it wasn't the basic programming that had me stuck - it was the GUI element. I had a working command line game within a day; however, that is not what this project asked for. I would like to improve my grasp of Pygame and SimpleGE; I am not a game developer, but it was fun to get creative on the programming front. Next time, perhaps in my next CS class, I hope to gain a better understanding of the small details. I strayed very far from the original Game Design Document; I had big, ambitious plans. I did my best to stay on track by taking a couple of hours out of my day every day to work on the project. 

Game complete: December 4, 2025