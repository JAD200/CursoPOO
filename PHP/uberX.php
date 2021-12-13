<?php
require_once('./car.php');
class UberX extends Car {
    public $brand;
    public $model;

    public function __construct($license, $driver, $brand, $model){
        parent::__construct($license,$driver);
        $this->brand = $brand;
        $this->model = $model;
    }
    //? frunction inherited from printDataCar in Car.php
    public function printDataCar() {
        parent::printDataCar(); //  This shows the model and the brand of an UberX
        echo"<br>
        Modelo: $this->model
        Marca: $this->brand
        ";
    }
}
?>