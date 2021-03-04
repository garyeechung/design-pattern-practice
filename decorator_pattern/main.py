from starbuzz.beverage import DarkRoast, Espresso, HomeBlend
from starbuzz.condiment import Mocha, Soy, Whip


beverage1 = Espresso()
print(f"{beverage1.description} ${beverage1.cost}")

beverage2 = DarkRoast()
beverage2 = Mocha(beverage2)
beverage2 = Mocha(beverage2)
beverage2 = Whip(beverage2)
print(f"{beverage2.description} ${beverage2.cost}")

beverage3 = HomeBlend()
beverage3 = Soy(beverage3)
beverage3 = Mocha(beverage3)
beverage3 = Whip(beverage3)
print(f"{beverage3.description} ${beverage3.cost}")
