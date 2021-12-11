package Java;

class UberPool extends Car {
    String brand;
    String model;

    public UberPool(String license, Account driver, String brand, String model) {
        //? "super" makes reference to atributes and methods of the super class or father class
        super(license, driver);
        //? While "this" makes reference to the class you are right know or the child class
        this.brand = brand;
        this.model = model;
    }
}
