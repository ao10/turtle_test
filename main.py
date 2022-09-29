# We have to import pygame to use it
import pygame

# All pygame programs must init before using its library
pygame.init()

# Set variables for our window size
windowwidth = 400
windowheight = 400
# Create our window
win = pygame.display.set_mode((windowwidth, windowheight))
# Set our window's title bar
pygame.display.set_caption("Python Platformer")
# Define our run variable, when this becomes False the window will close and the program will end
run = True
# Run our core game loop: right now this does nothing except keep the window open
while run:
    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # This is where most of our game code would go!

    # Update the pygame display with whatever we drew on the screen this time through the loop
    # If you forget this line of code you'll only ever see a black window
    pygame.display.update()
