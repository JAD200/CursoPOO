/* function Payment() {
    this.id;
} */

//* EcmaScript6
class Payment {
    constructor(id) {
        this.id = id;
    }

    showPayment() {
            console.log('Payment id: ' + this.id)
    }
}