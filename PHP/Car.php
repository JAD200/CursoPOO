<?php

require_once('./Account.php');

class Car {
    private $id         = integer;
    private $license    = string;
    private $driver     = string;
    private $passengers = integer;

    public function __contruct($license, $driver)
    {
        $this->license=$license;
        $this->driver=$driver;
    }

    public function setPassengers($passengers)
    {
        $this->passengers=$passengers;
    }

    public function getLicense()
    {
        return $this->license;
    }

    public function getDriver()
    {
        return $this->driver;
    }

}
?>