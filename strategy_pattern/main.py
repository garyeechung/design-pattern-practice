from duck.ducks import MallarDuck, ModelDuck, RobberDuck
from duck.flybehaviors import FlyNoWay

if __name__ == "__main__":
    mallarduck = MallarDuck()
    mallarduck.perform_fly()
    mallarduck.set_fly_behavior(FlyNoWay)
    mallarduck.perform_fly()
    mallarduck.perform_quack()

    robber = RobberDuck()
    robber.perform_fly()
    robber.perform_quack()

    model = ModelDuck()
    model.perform_fly()
    model.perform_quack()
