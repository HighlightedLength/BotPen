import pygame, pygame.gfxdraw

triangle_pts = [(0,0),(9,5),(0,9)]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Agent(pygame.sprite.Sprite):
    def __init__(self, color1, color2, state, radius = 4):
        super(Agent, self).__init__()

        width = radius * 2 + 1

        #create the image of the sprite
        self.base_image = pygame.Surface([width,width], pygame.SRCALPHA, 32).convert_alpha()
        self.base_image.fill((0,0,0,0))
        """
        for i in range(0,radius + 1):
            pygame.gfxdraw.aacircle(self.base_image, 4,4,i,color1)
        """

        pygame.draw.circle(self.base_image, color1, (radius, radius), radius)
        pygame.draw.line(self.base_image, color2, (radius, radius), (radius*2, radius))

        #rotate the base image
        self.image = pygame.transform.rotate(self.base_image, state[2])

        #set reference to image rect
        self.rect = self.image.get_rect()

        #set the position of the sprite
        self.rect.center = state[:2]

    def set_state(self, state):
        #rotate the base image
        self.image = pygame.transform.rotate(self.base_image, state[2])

        #set reference to image rect
        self.rect = self.image.get_rect()

        #set the position of the sprite
        self.rect.center = state[:2]




def main():

    #setting up the window
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()

    #render the display?
    pygame.display.flip()

    #add the agents
    agent_smith = Agent(RED, WHITE, (200,150,0),10)
    sprite_list = pygame.sprite.Group()
    sprite_list.add(agent_smith)
    angle = 0

    done = False

    while not done:
            #check to quit
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            done = True

            #update the sprite
            angle += 22.5
            agent_smith.set_state((100,250,angle))

            sprite_list.draw(screen)
            #screen.set_at((200,150), BLUE)

            clock.tick(12)
            pygame.display.flip()
            screen.fill(BLACK)

if __name__ == "__main__":
    main()
