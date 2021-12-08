from car import Car
from account import Account


def run():
    print('Car class')
#   Car1
    car = Car("AMS321", Account("Andres Herrera", "45613A"))
    print(vars(car))
    print(vars(car.driver))
#   Car2
    car2 = Car("GFS851", Account("Paula Herrera", "45612B"))
    print(vars(car2))
    print(vars(car2.driver))


if __name__ == '__main__':
    run()