from car import Car
from account import Account
from uberX import UberX


def run():
    print('Car class')
#   Car1
    car = Car("AMS321", Account("Andres Herrera", "45613A"))
    print('\n', vars(car))
    print(vars(car.driver))
#   Car2
    car2 = Car("GFS851", Account("Paula Herrera", "45612B"))
    print('\n', vars(car2))
    print(vars(car2.driver))
#   UberX
    car3 = UberX("AMS321", Account("Andres Herrera", "45613A"), 'Hyundai', 'H1')
    print('\n', vars(car3))
    print(vars(car3.driver))

if __name__ == '__main__':
    run()