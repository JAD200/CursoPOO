# Account family
from account import Account
from user import User
from driver import Driver
# Car family
from car import Car
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

def print_account_data(account_name):
    print('\n Accounr ID:', account_name.id)
    print(vars(account_name))

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
#   Account
    print('\n\t Account family')
    #   User
    user = User(456123, 'Jose Hernandez', 'YTl465', 'myemail@mail.com', 'password')
    print_account_data(user)
    #   Driver
    driver = Driver(456132, 'Pedro Hernandez', 'LJHB953', 'your@gmail.com', 'wordpass')
    print_account_data(driver)

if __name__ == '__main__':
    run()