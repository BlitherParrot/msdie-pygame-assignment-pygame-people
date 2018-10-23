import random, pygame

# Initialize Window
win = pygame.display.set_mode((500, 500))


# dice class
class dice:
    # Constructor
    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = random.randint(1, self.sides)

    def getValue(self):
        # Draws dies with 1 dot if value is 1
        if self.value == 1:
            # Preset colours
            white = (255, 255, 255)
            black = (0, 0, 0)
            bg_colour = (212, 76, 134)
            pygame.draw.rect(screen, bg_colour, (0, 0, 500, 500))  # Draws the background
            pygame.draw.rect(screen, white, (100, 100, 300, 300))  # Draws the back of the die in white
            pygame.draw.circle(screen, black, (250, 250), 25)  # Draws one black dot in center
        if self.value == 2:
            pygame.draw.rect(screen, (255, 255, 255), [100, 100, 300, 300])
            pygame.draw.circle(screen, (0, 0, 0), (175, 175), 50, 0)
            pygame.draw.circle(screen, (0, 0, 0), (325, 325), 50, 0)
        if self.value == 3:
            pygame.draw.rect(win, (0, 0, 0), ((0, 0), (500, 500)), 1)
            pygame.draw.circle(win, (0, 0, 0), (250, 250), (50))
            pygame.draw.circle(win, (0, 0, 0), (125, 125), (50))
            pygame.draw.circle(win, (0, 0, 0), (375, 375), (50))
        if self.value == 4:
            pygame.draw.circle(win, (0,0,0), (100, 100), 50, 50)
            pygame.draw.circle(win, (0,0,0), (400, 100), 50, 50)
            pygame.draw.circle(win, (0, 0, 0), (100, 400), 50, 50)
            pygame.draw.circle(win, (0, 0, 0), (400, 400), 50, 50)
        if self.value == 5:
            # Initialize radius, diameter ( 2 * d )
            r = 40
            d = 2 * r

            # Draw 5 circle, radius r, offset d from the sides
            pygame.draw.circle(win, (0, 0, 0), (d, d), r)
            pygame.draw.circle(win, (0, 0, 0), (500 - d, 500 - d), r)
            pygame.draw.circle(win, (0, 0, 0), (d, 500 - d), r)
            pygame.draw.circle(win, (0, 0, 0), (500 - d, d), r)
            pygame.draw.circle(win, (0, 0, 0), (250, 250), r)

    def setValue(self, value):
        self.value = value
