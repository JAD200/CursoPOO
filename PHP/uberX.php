<?php
class UberX extends Car {
    public $brand;
    public $model;

    public function __contruct($license, $driver, $brand, $model){
        parent::__contruct($license, $driver);
        $this->brand = $brand;
        $this->model = $model;
    }
}
?>