package Java;

class Car {
    Integer id;
    String license;
    Account driver;
    private Integer passengers;

    public Car(String license, Account driver){
        this.license = license;
        this.driver = driver;
    }

    void printDataCar() {
        if(passengers != null)
            System.out.println("license: " + license + " Driver: " + driver.name + " Passengers: " + passengers);
    }

    public Integer getPassenger() {
        return passengers;
    }

    public void setPassenger(Integer passenger) {
        if (passenger == 4) {
            this.passengers = passenger;
        } else {
            System.out.println("Necesitas asignar 4 pasajeros");
        }
    }
}
