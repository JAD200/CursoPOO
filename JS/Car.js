/* function Car(license, driver) {
    this.id;
    this.license = license;
    this.driver = driver;
    this.passenger;
}

Car.prototype.printDataCar = function() {
    console.log(this.driver)
    console.log(this.driver.name)
    console.log(this.driver.document)
} */

//* EcmaScript6
class Car {
    constructor(license, driver) {
        this.id;
        this.license = license;
        this.driver = driver;
        this.passenger;
    }
    printDataCar() {
        console.group('Car data')
        if (this.brand == undefined)
            console.table(this.driver);
        else {
                console.table(this.driver);
                console.log('Brand: ' + this.brand, '\nModel: ' + this.model);
            }
        console.groupEnd()
    }
}
