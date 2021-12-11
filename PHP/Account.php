<?php

class Account {
    private $id = integer;
    private $name = string;
    private $document = string;
    private $email = string;
    private $password = string;

    public function __construct($name, $document) {
        $this->name=$name;
        $this->document=$document;
    }
    public function getDocument()
    {
        return $this->document;
    }

    public function getName()
    {
        return $this->name;
    }
}
?>