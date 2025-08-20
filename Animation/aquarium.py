import pygame


# -----Fish Class----------------------------------------------------------------------------------
# I can't seem to find a way to import this class from fish.py, so i copied it here...
# Need to learn how to do that...
class Fish:
    def __init__(self, window, name, color, triangleList):
        self.window = window
        self.name = name
        self.triangleList = triangleList
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.color}"

    # draw all the triangles parts of the fish and make a black border lookalike
    def draw(self):
        for i in range(0, len(self.triangleList)):
            pygame.draw.polygon(self.window, self.color, self.triangleList[i])
            pygame.draw.polygon(self.window, black, self.triangleList[i], 2)


# -----Functions to create the fishes --------------------------------------------------------------
points = [
    ((100, 100), (100, 200), (200, 100)),
    ((0, 50), (50, 75), (75, 0)),
    ((100, 100), (200, 100), (100, 0)),
]
red = (255, 0, 0)
black = (0, 0, 0)


def initFish():
    f1 = Fish(window, "DO", red, points)
    f1.draw()


# --------------------------------------------------------------------------------------------------
# -------Create the window--------------------------------------------------------------------------

# Initialise pygame
pygame.init()

# Create a window
(width, height) = (600, 500)
window = pygame.display.set_mode((width, height))

# Set window's caption // and icon
pygame.display.set_caption("Aquazik")
# icon = pygame.image.load('....png')
# pygame.display.set_icon(icon)

# Set window's background color once
bgColor = (255, 255, 255)
# pygame.display.update()


# ---Loop, update display and quit------------------------------------------------------------------

run = True
# Loop that updates the display
while run:
    window.fill(bgColor)
    pygame.draw.polygon(window, red, points[1])

    initFish()
    for event in pygame.event.get():
        # quit if click quit
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit
exit()
