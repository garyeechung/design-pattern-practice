from duck.ducks import MallarDuck, RobberDuck
from duck.flybehaviors import FlyNoWay

if __name__ == "__main__":
    md = MallarDuck()
    md.perform_fly()
    md.set_fly_behavior(FlyNoWay)
    md.perform_fly()
    md.perform_quack()

    rb = RobberDuck()
    rb.perform_fly()
    rb.perform_quack()
