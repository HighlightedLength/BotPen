from view import stencils

GREEN = (0, 255, 0, 255)
WHITE = (255, 255, 255, 127)
color1 = GREEN
color2 = WHITE

class AgentService:
    base_image = None
    world_height = None

    def setup(self, screen, config):
        visuals = config.get('visuals') or {}
        self.radius = visuals.get('radius') or 4
        self.width = visuals.get('width') or self.radius * 2 + 1
        self.scale = visuals.get('scale') or 1

        for agent in config['agents']:
            stencils.directed_circle(
                screen,
                agent['x0'], agent['y0'], agent['theta0'],
                self.radius, self.scale, color1)

    def render(self, screen, agent, odometry, scale):
        #draw real location
        stencils.directed_circle(screen,
            agent.x, agent.y, agent.theta,
            self.radius, self.scale, color1)

        #draw observation
        stencils.directed_circle(screen,
            agent.x + odometry.noise_dx,
            agent.y + odometry.noise_dy,
            agent.theta + odometry.noise_dtheta,
            self.radius, self.scale, color2)
