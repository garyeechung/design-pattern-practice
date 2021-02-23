import unittest

from ..duck import ducks
from ..duck import flybehaviors, quackbehaviors


class TestMallarDuck(unittest.TestCase):

    def setUp(self):
        self.mallarduck = ducks.MallarDuck()

    def test_repr(self):
        self.assertEqual(self.mallarduck.__repr__(), "I am a MallarDuck")

    def test_perform_fly(self):
        self.assertEqual(self.mallarduck.perform_fly(), "I fly with wings")

    def test_set_fly_behavior(self):
        self.mallarduck.flybehavior = flybehaviors.FlyWithRocket()
        self.assertEqual(self.mallarduck.perform_fly(), "I fly with a rocket")

    def test_perform_quack(self):
        self.assertEqual(self.mallarduck.perform_quack(), 'quack')

    def test_set_quack_behavior(self):
        self.mallarduck.quackbehavior = quackbehaviors.MuteQuack()
        self.assertEqual(self.mallarduck.perform_quack(), '<<silence>>')


if __name__ == "__main__":
    unittest.main()
