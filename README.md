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
    - self.display - sets display size (1280, 720)
    - self.lblOut - prompts user "what will you do? 1/2"
    - self.txtName - takes user input
    - self.btnClickMe - tells computer that user input is received
Initializer creates components:
init:
    set lblOut center to 640, 400
    set lblOut size to 300, 30
    set lblOut text to "what will you do? 1/2"
    set lblOut bgColor to purple

    set txtName center to 640, 550
    set txtName text to ""

    set btnClickMe center to (640, 600)
    set btnClickMe text to "click me" 

    sprite list: self.lblOut, self.txtName, self.btnClickMe

process event:
    assign user input to txtName text

process:
    if btnClickMe clicked:
        bgColor set to purple (for testing purposes)
        choice gets self.txtName.text
        if choice is 1, nextKey is choiceA
        if choice is 2, nextKey is choiceB
        else nextKey is currentKey
    return nextKey

    keepGoing gets True
    begin while loop
        if currentKey == "start":
            (layout of all key sprites):
            center - 640, 250
            size - 800, 300
            bgColor - white
            textLines - varies between sprites
        each if statement gets its own sprite list, IE:
        self.sprites = [self.questionStart]... and so on for every statement
    
    if statements/sprites: start/questionStart, left/questionLeft, right/questionRight, stow/questionStow, drop/questionDrop, keep/questionKeep, throw/questionThrow, remember/questionRem, onward/questionOnward, follow/questionFollow, tower/questionTower, scent/questionScent, pretend/questionPretend, gouda/questionGouda, bleu/questionBleu, go/questionGo, farmer/questionFarmer, goBleu/questiongoBleu, quit

    while loop ends if currentKey gets "quit"

CITATIONS:
    none
    *I was going to use photos from Open Clip Art, but did not get everything working before the due date.

PROCESS & REFLECTION:
    This project showed me just how difficult game development is for intermediate programmers. I considered myself decently fluent in Python before taking this class, but now I know that my knowledge is just the tip of the iceberg. To be fair, it wasn't the basic programming that had me stuck - it was the GUI element. I had a working command line game within a day; however, that is not what this project asked for. Eventually I had to entirely rework my code to integrate graphical elements, which was the beginning of this project's downfall. I would like to improve my grasp of Pygame and SimpleGE; I am not a game developer and never have been, but it was fun to get creative on the programming front. Next time, perhaps in my next CS class, I hope to gain a better understanding of everything, even if that means going back and studying lectures from weeks ago. I strayed very far from the original Game Design Document; I had big, ambitious plans. I did my best to stay on track by taking a couple of hours out of my day every day to work on the project. 