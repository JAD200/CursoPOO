# Car family
from car import Car
from account import Account
from uberX import UberX
# Payment family
from payment import Payment
from card import Card

def print_car_data(car_name):
    print('\n', vars(car_name))
    print(vars(car_name.driver))

def print_payment_data(payment_name):
    print('\n Payment ID:', payment_name.id)
    print(vars(payment_name))

def run():
#   Car
    print('\n\t Car family')

    car = Car("AMS321", Account("Andres Herrera", "45613A"))
    print_car_data(car)
    #   Car2
    car2 = Car("GFS851", Account("Paula Herrera", "45612B"))
    print_car_data(car2)
    #   UberX
    car3 = UberX("AMS321", Account("Andres Herrera", "45613A"), 'Hyundai', 'H1')
    print_car_data(car3)
#   Payment
    print('\n\t Payment family')
    #   Card
    payment = Card(4565123, '4424 4566 4951 4695', '7/7/12', 456)
    print_payment_data(payment)
    #   Cash
    payment1 = Payment(465129)
    print_payment_data(payment1)



if __name__ == '__main__':
    run()