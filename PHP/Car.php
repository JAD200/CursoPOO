<?php
require_once('account.php');
class Car {
    //* Declaration of atributes
    private $id;
    private $license;
    private $driver;
    protected $passenger;

    public function __construct($license, $driver){
        $this->license = $license;
        $this->driver = $driver;
    }

    public function printDataCar() {
        if ($this->passenger != null){
            echo "
            - Licencia: $this->license
            Driver: {$this->driver->name}
            Número de pasajeros: $this->passenger  ";
        }
    }

    public function getPassenger() {
        return $this->passenger;
    }

    public function setPassenger($passenger) {

        if ($passenger == 4) {
            $this->passenger = $passenger;
        }
        else {
            echo "Necesitas asignar 4 pasajeros";
        }
    }
}
?>
