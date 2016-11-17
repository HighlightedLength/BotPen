from view import stencils


class EstimationService:
    radius = None
    width = None
    scale = None

    def __init__(self, estimation_type, color):
        self.estimation_type = estimation_type
        self.color = color

    def is_applicable(self, estimation_type):
        return self.estimation_type == estimation_type

    def setup(self, screen, config):
        visuals = config.get('visuals') or {}
        self.radius = visuals.get('radius') or 4
        self.width = visuals.get('width') or self.radius * 2 + 1
        self.scale = visuals.get('scale') or 1


        for agent in config['agents']:
            stencils.directed_circle(
                screen,
                agent['x0'], agent['y0'], agent['theta0'],
                self.radius, self.scale, self.color)

    def render(self, screen, estimates, agents, scale):
        for estimate in estimates.values():
            agent = agents[estimate.agent_id]
            stencils.directed_circle(screen,
                estimate.x, estimate.y, estimate.theta,
                self.radius, self.scale, self.color)
            stencils.line(screen,
                estimate.x, estimate.y, agent.x, agent.y, self.scale, self.color)
