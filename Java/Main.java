package Java;

class Main {
    public static void main(String[] args) {
        System.out.println("Car class");
        Car car = new Car();
        car.license = "AMQ132";
        car.driver = "Andres Herrera";
        car.passengers = 4;
        car.printDataCar();

        Car car2 = new Car();
        car2.license = "QWF462";
        car2.driver = "Paula Herrera";
        car2.passengers = 3;
        car2.printDataCar();
    }
}