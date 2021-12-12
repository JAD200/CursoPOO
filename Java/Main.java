package Java;

class Main {
    public static void main(String[] args) {
        System.out.println("Car class");
        UberX uberX = new UberX("AMQ132", new Account("Andres Herrera", "AND123"), "Chevrolet", "Sonic");
        uberX.setPassenger(3);
        uberX.printDataCar();

        /* Car car2 = new Car("QWF462", new Account("Paula Herrera", "PHN456"));
        car2.printDataCar();

        System.out.println("Payment class");
        Payment payment = new Payment(13213);
        payment.printPaymentData(); */
    }
}