<?php
//* Requiriment of the classes
require_once("account.php");
require_once("car.php");
require_once("uberPool.php");
require_once("uberX.php");
require_once("./uberBlack.php");
require_once("./uberVan.php");

// Cretation of an object for class UberX
echo "<h4>UberX</h4>";
$uberX = new UberX("CVB123", new Account("Andres Herrera", "AND456"), "Chevrolet", "Spark");
$uberX->setPassenger(4);
$uberX->printDataCar();
// Cretation of an object for class UberPool
echo "<h4>UberPool</h4>";
$uberPool = new UberPool("TYU567", new Account("Andrea Ferran", "ANDA765"), "Dodge", "Attitude");
$uberPool->setPassenger(4);
$uberPool->printDataCar();
// Cretation of an object for class UberVan
echo "<h4>UberVan</h4>";
$uberVan = new UberVan("OJL395", new Account("Raúl Ramírez", "AND456"), "Nissan", "Versa");
$uberVan->setPassenger(6);
$uberVan->printDataCar();
?>