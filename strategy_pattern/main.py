from duck.ducks import MallarDuck
from duck.flybehaviors import FlyNoWay

if __name__ == "__main__":
    md = MallarDuck()
    md.perform_fly()
    md.set_fly_behavior(FlyNoWay)
    md.perform_fly()
