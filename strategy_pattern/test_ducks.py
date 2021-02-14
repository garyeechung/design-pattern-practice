import unittest

from duck import ducks
from duck import flybehaviors, quackbehaviors


class TestMallarDuck(unittest.TestCase):

    def setUp(self):
        self.mallarduck = ducks.MallarDuck()

    def test_repr(self):
        self.assertEqual(self.mallarduck.__repr__(), "I am a MallarDuck")

    def test_perform_fly(self):
        self.assertEqual(self.mallarduck.perform_fly(), "I fly with wings")

    def test_set_fly_behavior(self):
        self.mallarduck.set_fly_behavior(flybehaviors.FlyWithRocket)
        self.assertEqual(self.mallarduck.perform_fly(), "I fly with a rocket")

    def test_perform_quack(self):
        self.assertEqual(self.mallarduck.perform_quack(), 'quack')

    def test_set_quack_behavior(self):
        self.mallarduck.set_quack_behavior(quackbehaviors.MuteQuack)
        self.assertEqual(self.mallarduck.perform_quack(), '<<silence>>')


class TestRobberDuck(unittest.TestCase):

    def setUp(self):
        self.robberduck = ducks.RobberDuck()

    def test_repr(self):
        self.assertEqual(self.robberduck.__repr__(), "I am a RobberDuck")

    def test_perform_fly(self):
        self.assertEqual(self.robberduck.perform_fly(), "I cannot fly")

    def test_set_fly_behavior(self):
        self.robberduck.set_fly_behavior(flybehaviors.FlyWithRocket)
        self.assertEqual(self.robberduck.perform_fly(), "I fly with a rocket")

    def test_perform_quack(self):
        self.assertEqual(self.robberduck.perform_quack(), 'squeak')

    def test_set_quack_behavior(self):
        self.robberduck.set_quack_behavior(quackbehaviors.MuteQuack)
        self.assertEqual(self.robberduck.perform_quack(), '<<silence>>')


class TestModelDuck(unittest.TestCase):

    def setUp(self):
        self.modelduck = ducks.ModelDuck()

    def test_repr(self):
        self.assertEqual(self.modelduck.__repr__(), "I am a ModelDuck")

    def test_perform_fly(self):
        self.assertEqual(self.modelduck.perform_fly(), "I cannot fly")

    def test_set_fly_behavior(self):
        self.modelduck.set_fly_behavior(flybehaviors.FlyWithRocket)
        self.assertEqual(self.modelduck.perform_fly(), "I fly with a rocket")

    def test_perform_quack(self):
        self.assertEqual(self.modelduck.perform_quack(), '<<silence>>')

    def test_set_quack_behavior(self):
        self.modelduck.set_quack_behavior(quackbehaviors.Quack)
        self.assertEqual(self.modelduck.perform_quack(), 'quack')


if __name__ == "__main__":
    unittest.main()
