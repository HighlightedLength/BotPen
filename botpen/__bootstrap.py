from aglyph.binder import Binder
from aglyph.component import Reference
from random import Random

def bootstrap(config, output_path):
    container = Binder()
    rng = __build_rng(config)

    renderer = __bind_view_components(container, config)

    (container.bind("logistics.Logger",
            to = "logistics.Logger"))

    (container.bind("AppEngine",
            to = "botpen.AppEngine",
            strategy = "singleton")
        .init(
            config,
            Reference("app.Controller"),
            renderer,
            Reference("view.Logger")))

    (container.bind("app.Controller",
            to = "botpen.app.Controller",
            strategy = "singleton")
        .init(
            Reference("domain.AgentService"),
            Reference("domain.WorldService"),
            Reference("logistics.Logger")
        ))
    (container.bind("view.Logger",
            to = "botpen.view.services.Logger",
            strategy = "singleton"))

    (container.bind("domain.AgentService",
            to = "botpen.domain.services.AgentService",
            strategy = "singleton")
        .init(
            Reference("domain.AgentFactory"),
            Reference("domain.BehaviorFactory"),
            Reference("domain.MoveFactory"),
            Reference("domain.ObsFactory"),
            Reference("domain.EstimationFactory"),
            Reference("logistics.AgentRepo")
        ))
    (container.bind("domain.WorldService",
            to = "botpen.domain.services.WorldService")
        .init(
            Reference("logistics.WorldRepo")
        ))


    estimation_strategies = __bind_estimation_strategies(container, config)
    __bind_factories(container, config, rng, estimation_strategies)
    __bind_behavior_components(container, config)
    __bind_repos(container)

    return container

def __build_rng(config):
    rng_seed = config.get('rng_seed')
    return Random(rng_seed) if rng_seed else Random()

def __bind_factories(container, config, rng, estimation_strategies):
    (container.bind("domain.AgentFactory",
            to = "botpen.domain.factories.AgentFactory",
            strategy = "singleton")
        .init(
            Reference("logistics.AgentRepo")
        ))
    (container.bind("domain.BehaviorFactory",
            to = "botpen.domain.factories.BehaviorFactory",
            strategy = "singleton")
        .init(
            Reference("logistics.AgentRepo"),
            Reference("domain.behavior.Resolver")
        ))
    (container.bind("domain.MoveFactory",
            to = "botpen.domain.factories.MoveFactory",
            strategy = "singleton")
        .init(
            rng,
            Reference("logistics.AgentRepo")
        ))
    (container.bind("domain.ObsFactory",
            to = "botpen.domain.factories.ObservationFactory",
            strategy = "singleton")
        .init(
            rng,
            Reference("logistics.AgentRepo")
        ))

    (container.bind("domain.EstimationFactory",
            to = "botpen.domain.factories.EstimationFactory",
            strategy = "singleton")
        .init(*estimation_strategies))

def __bind_repos(container):
    (container.bind("logistics.AgentRepo",
            to = "botpen.logistics.repos.AgentRepo",
            strategy = "singleton"))
    (container.bind("logistics.ParametricBehaviorRepo",
            to = "botpen.logistics.repos.ParametricBehaviorRepo",
            strategy = "singleton"))
    (container.bind("logistics.WorldRepo",
            to = "botpen.logistics.repos.WorldRepo",
            strategy = "singleton"))

def __bind_behavior_components(container, config):
    (container.bind("domain.behavior.ParametricConstants",
            to = "botpen.domain.behavior_resolvers.ParametricConstantsResolver")
        .init(
            Reference("logistics.ParametricBehaviorRepo")
        ))

    resolvers = [Reference("domain.behavior.ParametricConstants")]

    (container.bind("domain.behavior.Resolver",
            to = "botpen.domain.behavior_resolvers.DecidingResolver")
        .init(
            *resolvers
        ))
def __bind_estimation_strategies(container, config):
    (container.bind("domain.OdometryEstimator",
            to = "botpen.domain.estimation_strategies.OdometryEstimator",
            strategy = "singleton")
        .init(
            Reference("logistics.OdometryEstimationRepo")
        ))
    (container.bind("logistics.OdometryEstimationRepo",
            to = "botpen.logistics.repos.EstimationRepo",
            strategy = "singleton"))

    (container.bind("domain.FormationEstimator",
            to = "botpen.domain.estimation_strategies.FormationEstimator",
            strategy = "singleton")
        .init(
            Reference("logistics.FormationEstimationRepo")
        ))
    (container.bind("logistics.FormationEstimationRepo",
            to = "botpen.logistics.repos.EstimationRepo",
            strategy = "singleton"))

    (container.bind("domain.KalmanEstimator",
            to = "botpen.domain.estimation_strategies.KalmanEstimator",
            strategy = "singleton"))

    return [
        Reference("domain.OdometryEstimator"),
        Reference("domain.FormationEstimator"),
        Reference("domain.KalmanEstimator")]

def __bind_view_components(container, config):
    if config.get('view_on'):
        (container.bind("view.AgentService",
                to = "botpen.view.services.AgentService",
                strategy = "singleton"))

        (container.bind("view.OdometryEstimationService",
                to = "botpen.view.services.EstimationService",
                strategy = "singleton")
            .init("Odometry",(127,127,255,255)))
        (container.bind("view.FormationEstimationService",
                to = "botpen.view.services.FormationEstimationService",
                strategy = "singleton")
            .init((255,63,63,255)))
        (container.bind("view.KalmanEstimationService",
                to = "botpen.view.services.EstimationService",
                strategy = "singleton")
            .init("Kalman",(255,0,255,255)))

        estimation_services = [
            Reference("view.OdometryEstimationService"),
            Reference("view.FormationEstimationService"),
            Reference("view.KalmanEstimationService")]

        (container.bind("view.Renderer",
                to = "botpen.view.Renderer",
                strategy = "singleton")
            .init(
                Reference("view.AgentService"),
                *estimation_services
            ))
        return Reference('view.Renderer')
    else:
        return None
