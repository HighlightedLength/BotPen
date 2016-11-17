from domain.models import Procedure, Lifecycle

class WorldService:
    def __init__(self, world_repo):
        self.world_repo = world_repo

    def setup(self, config):
        size = config['world']['size']
        self.world_repo.set_size((size[0],size[1]))

        procedure = config['world'].get('initial_procedure')
        if procedure == None or procedure == 'auto':
            self.world_repo.set_procedure(Procedure.auto)
        elif procedure == 'step':
            self.world_repo.set_procedure(Procedure.step)
        elif procedure == 'pause':
            self.world_repo.set_procedure(Procedure.pause)
        else:
            self.world_repo.set_procedure(Procedure.finish)

        self.world_repo.set_time(0)
        self.world_repo.set_time_limit(config['world']['limit'])

    def get_lifecycle(self):
        procedure = self.world_repo.get_procedure()

        return Lifecycle(
                finish = procedure == Procedure.finish,
                proceed = procedure != Procedure.pause
            )

    def update_lifecycle(self, updates):
        procedure = self.world_repo.get_procedure()

        if updates.get('finish'):
            self.world_repo.set_procedure(Procedure.finish)
        elif updates.get('toggle_auto') and procedure == Procedure.pause:
            self.world_repo.set_procedure(Procedure.auto)
        elif updates.get('toggle_auto') or updates.get('pause'):
            self.world_repo.set_procedure(Procedure.pause)
        elif updates.get('step'):
            self.world_repo.set_procedure(Procedure.step)

    def step(self):
        time = self.world_repo.get_time()
        time += 1
        self.world_repo.set_time(time)

        if self.world_repo.get_procedure() == Procedure.step:
            self.world_repo.set_procedure(Procedure.pause)
        if time >= self.world_repo.get_time_limit():
            self.world_repo.set_procedure(Procedure.finish)
        return time
