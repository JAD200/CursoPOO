from car import Car

def run():
    print('Hola mundo')
    car = Car()
    car.license = "AMS321"
    car.driver = "Andres Herrera"
    print(vars(car))

    car2 = Car()
    car2.license = "GFS851"
    car2.driver = "Martha Herrera"
    print(vars(car2))

if __name__ == '__main__':
    run()