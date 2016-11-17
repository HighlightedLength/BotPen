from view import stencils

_CENTROID_COLOR = (255,255,255,127)
class FormationEstimationService:
    radius = None
    width = None
    scale = None

    def __init__(self, color):
        self.estimation_type = 'Formation'
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

    def render(self, screen, formation, agents, scale):
        estimates = formation['estimates']
        for estimate in estimates.values():
            agent = agents[estimate.agent_id]
            stencils.directed_circle(screen,
                estimate.x, estimate.y, estimate.theta,
                self.radius, self.scale, self.color)
            stencils.line(screen,
                estimate.x, estimate.y, agent.x, agent.y, self.scale, self.color)
        cx = formation['centroid_x']
        cy = formation['centroid_y']
        stencils.filled_circle(
            screen,
            cx,
            cy,
            3,
            self.scale,
            _CENTROID_COLOR
        )

        odometric = formation['odometric']
        for odo in odometric.values():
            stencils.directed_circle(screen,
                odo.x, odo.y, odo.theta,
                self.radius, self.scale, _CENTROID_COLOR)
            stencils.line(screen,
                odo.x, odo.y, cx, cy, self.scale, _CENTROID_COLOR)
