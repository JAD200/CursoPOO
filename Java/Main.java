package Java;

class Main {
    public static void main(String[] args) {
        System.out.println("Car class");
        Car car = new Car("AMQ132", new Account("Andres Herrera", "AND123"));
        car.passengers = 4;
        car.printDataCar();

        Car car2 = new Car("QWF462", new Account("Paula Herrera", "PHN456"));
        car2.passengers = 3;
        car2.printDataCar();
    }
}