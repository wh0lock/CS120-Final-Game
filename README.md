# CS120-Final-Game
This is a game in which the user makes their own decisions and their choices decide how the story will end. 
```
Game Design Document
Choose-Your-Own-Adventure (Graphical)

OVERVIEW
The premise is as follows: you are a bright eyed, hopeful adventurer looking for places to be and things to do. A weathered old wizard sends you on a quest to find an ancient relic, but he doesn't give you very many details to go on; all you have is a place to start. You go where he marked the map and are met with a fork in the road. What you choose will determine the success of your adventure.

STATE TRANSITION DIAGRAM
Please refer to State Transition Diagram.png.

THE INSTRUCTIONS SCENE
Please refer to Instructions Scene Diagram.png.
This controls access to the game. You will receieve instructions here. 
Elements:
- Title
    - lblTitle
    - simpleGE label with game title
- Instructions 
    - lblInstructions
    - simpleGE multilabel with gameplay instructions
- startButton
    - stock button to start the game
- quitButton
    - stock button to quit to desktop
Other attributes:
- response - string representing user's choice, read in main function
Initializer creates all attributes and sets up sprite list:
    set background image
    set default response to "quit"
    create instructions multilabel
    set instructions center and size
    create startButton
    set text to "start"
    set center
    create quitButton
    set text to "quit"
    set center
    sprite list: lblTitle, lblInstructions, quitButton, startButton
Process method/event handling:
    if quit button is pressed,
        response gets "quit"
        stop the scene
    if play button is pressed,
        response gets "play"
        stop the scene

THE GAME CLASS
Please refer to Game Scene Diagram.png.
Primary class. Subclassed from simpleGE.Scene.
Visual attributes:
    - player - an instance of the Player class
    - lblQuestion - an instance of the LblQuestion class
    - choiceA - an instance of the ChoiceA class
    - choiceB - an instance of the ChoiceB class
    - lblResult - an instance of the LblResult class
Non-sprite assets:
    - backgroundSound - stock instance of the simpleGE.Sound class.
Initializer creates components:
init:
    set image to background image
    create instance of LblQuestion -> lblQuestion
    create instance of Player -> player
    create instance of ChoiceA -> choiceA
    create instance of ChoiceB -> choiceB
    create insatnce of LblResult -> lblResult
    sprite list: player, lblQuestion, choiceA, choiceB, lblResult
process:
    *TBD*

COMPONENTS OF GAME CLASS
Player
    Player is a subclass of simpleGE.Sprite
    The image is *TBD*
    Size should be *TBD*
    Transparent background crucial
    Starting position: bottom left of screen
    moveSpeed attribute is int, starts at 5
    init:
        set image to *TBD*
        set size to *TBD*
        set position to bottom left
        set moveSpeed to 5
    process:
        if left key is pressed, subtract moveSpeed from x
        if right key is pressed, add moveSpeed to x
        if up key is pressed, subtract moveSpeed from y
        if down key is pressed, add moveSpeed to y

MILESTONE PLAN (Tentative)
1. Game scene with background image and music
2. Add basic Player sprite
3. Add keyboard motion to Player (left, right, up, down)
4. Create dictionary of story, nodes, choices, etc. (refer to adventure game)
5. Add collision effect bewteen Player and ChoiceA or ChoiceB
    a. If player collides with ChoiceA, result gets so and so and is displayed on screen, next question is presented
    b. If player collides with ChoiceB, result gets so and so and is displayed on screen, next question is presented
6. Add appropriate labels and buttonse
7. Add instructions class and state transitions

Still under construction as of 11/17/2025
```
    