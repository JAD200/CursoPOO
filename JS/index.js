let car = new Car('AW456', new Account('Andres Herrera', 'AHN123'));
car.passenger = 4;
car.printDataCar();

let uberX = new Uberx('AW456', new Account('Paula Herrera', 'PKO123'), 'Hyundai', 'H1');
uberX.passenger = 3;
uberX.printDataCar();

let payment = new Payment(4456456);
payment.showPayment();

let payment2 = new Card(4561283, '4424 4555 4556 7894', '4/12/25', 149)
payment2.showPayment();

let user2 = new User(456213, "Jose Ramirez", "INE001","jose@mail.com", "mypass");
user2.printAccountData(user2);

let driver2 = new Driver(879123, "Pedro Ramirez", "O8P945","pedro@gmail.com", "yourpass");
driver2.printAccountData(driver2);
