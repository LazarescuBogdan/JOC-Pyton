import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE=(255, 165, 0)

class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """
 
    def __init__(self, x, y, width, height, color):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
 
    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y],2)
 
    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

# --- Generate bonuses coord
def generate_coord(x,y):
    
    x=random.randint(30,670)
    y=random.randint(30, 470)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Joc de joc")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 350
y_coord = 250

vit=5
x_obst1=1
y_obst1=1
x_obst2=1
y_obst2=1
x_obst1=random.randint(30,670)
y_obst1=random.randint(30, 470)
x_obst2=random.randint(30,670)
y_obst2=random.randint(30, 470)
player_image = pygame.image.load("pac.png").convert()


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -vit
            elif event.key == pygame.K_RIGHT:
                x_speed = vit
            elif event.key == pygame.K_UP:
                y_speed = -vit
            elif event.key == pygame.K_DOWN:
                y_speed = vit
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT:
                x_speed = 0
            elif event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP:
                y_speed = 0
            elif event.key == pygame.K_DOWN:
                y_speed = 0
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
 
    # --- Game logic should go here

    """# --- Character not leave the screen space
    if x_coord>690: x_coord=685
    if x_coord<0: x_coord=5
    if y_coord>480: y_coord=475
    if y_coord<0: y_coord=5
    """

    # ---Character speed changes
    if x_coord>x_obst1-10 and x_coord<x_obst1+20 and y_coord>y_obst1-20 and y_coord<y_obst1+15 :
        if vit<=10: vit+=2
        x_obst1=random.randint(30,670)
        y_obst1=random.randint(30, 470)
        
    if x_coord>x_obst2-10 and x_coord<x_obst2+20 and y_coord>y_obst2-20 and y_coord<y_obst2+15 :
        if vit>=2:vit-=2
        x_obst2=random.randint(30,670)
        y_obst2=random.randint(30, 470)
     
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    
    wall_list = pygame.sprite.Group()
    wall = Wall(0, 0, 10, 500,RED)
    wall_list.add(wall)
    wall = Wall(10,0,690,10,GREEN)
    wall_list.add(wall)


    pygame.draw.ellipse(screen, GREEN, [x_obst1, y_obst1, 20, 20], 0)
    pygame.draw.ellipse(screen, ORANGE, [x_obst2, y_obst2, 20, 20], 0)
    draw_stick_figure(screen, x_coord, y_coord)
    #screen.blit(player_image, [x_coord,y_coord])
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Viteza: "+str(vit), True, BLACK)

    screen.blit(text, [10, 10])
    wall_list.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
