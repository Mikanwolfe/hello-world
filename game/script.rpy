﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Ex", color="#ee3333")
image bg library = "bg library.jpg"
transform slightleft:
  xalign 0.1
  yalign -1.0

transform slightright:
  xalign 0.1
  yalign 0.5

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg library
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    e "This is before alignment"
    show ex at slightleft with dissolve

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    e "Some Major changes should've happened"
    
    e "though this is more of a test of whether or not I can github"

    # This ends the game.

    return
