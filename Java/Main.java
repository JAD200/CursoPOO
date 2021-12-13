package Java;

class Main {
    public static void main(String[] args) {
        System.out.println("Car class");
        UberX uberX = new UberX("AMQ132", new Account("Andres Herrera", "AND123"), "Chevrolet", "Sonic");
        uberX.setPassenger(4);
        uberX.printDataCar();

        UberVan uberVan = new UberVan("FGH753", new Account("Andres Herrera", "AND123"));
        uberVan.setPassenger(6);
        uberVan.printDataCar();

        /*System.out.println("Payment class");
        Payment payment = new Payment(13213);
        payment.printPaymentData();
        */
    }
}