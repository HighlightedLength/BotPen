import pygame
from pygame import gfxdraw
import math
BLACK = (0,0,0)

class Renderer:
    height = None
    width = None
    config = None
    scale = None

    def __init__(self, agent_service, *estimation_services):
        self.agent_service = agent_service
        self.estimation_services = list(estimation_services)


    def setup(self, config):
        self.world = config['world']
        self.visuals = config.get('visuals') or {}

        pygame.init()

        self.scale = scale = self.visuals.get('scale') or 1
        self.width = width = math.ceil(self.world['size'][0]/scale)
        self.height = height = math.ceil(self.world['size'][1]/scale)

        dim = (width,height)
        self.screen = pygame.display.set_mode(dim)
        self.clock = pygame.time.Clock()

        self.agent_service.setup(self.screen, config)
        for estimation_service in self.estimation_services:
            estimation_service.setup(self.screen, config)

        pygame.display.flip()

    def get_events(self):
        result = {}
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                result['finish'] = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    result['finish'] = True
                if event.key == pygame.K_SPACE:
                    result['toggle_auto'] = True
                if event.key == pygame.K_p:
                    result['pause'] = True
                if event.key == pygame.K_RETURN:
                    result['step'] = True
        return result

    def display(self, world):
        spf = self.visuals['steps_per_frame']
        fps = self.visuals['frames_per_second']

        if world['time'] % spf != 0:
            return

        self.clock.tick(fps)

        self.screen.fill(BLACK)

        odometries = world['observations'].odometries
        for agent in world['agents']:
            self.agent_service.render(self.screen, agent, odometries[agent.id], self.scale)

        agents = dict([(agent.id,agent) for agent in world['agents']])
        estimates = world['estimates']

        for estimation_type in estimates:
            renderer = (
                next(
                    (x for x in self.estimation_services
                        if x.is_applicable(estimation_type)),
                    None))
            if renderer:
                renderer.render(self.screen,estimates[estimation_type], agents,self.scale)

        font = pygame.font.Font(None, 36)
        text = font.render("Step: {0}".format(world['time']), 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.bottom = self.height
        textpos.right = self.width
        self.screen.blit(text, textpos)

        pygame.display.flip()

    def close(self):
        pygame.quit()
