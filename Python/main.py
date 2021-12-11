from car import Car
from account import Account
from uberX import UberX

def print_car_data(car_name):
    print('\n', vars(car_name))
    print(vars(car_name.driver))

def run():
    print('Car class')
#   Car1
    car = Car("AMS321", Account("Andres Herrera", "45613A"))
    print_car_data(car)
#   Car2
    car2 = Car("GFS851", Account("Paula Herrera", "45612B"))
    print_car_data(car2)
#   UberX
    car3 = UberX("AMS321", Account("Andres Herrera", "45613A"), 'Hyundai', 'H1')
    print_car_data(car3)

if __name__ == '__main__':
    run()