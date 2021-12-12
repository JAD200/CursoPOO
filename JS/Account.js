/* function Account(name, document) {
    this.id;
    this.name = name;
    this.document = document;
    this.email;
    this.password;
} */

//* EcmaScript6
class Account {
    constructor(name, document, email, password) {
        this.id;
        this.name = name;
        this.document = document;
        this.email;
        this.password;
    }

    printAccountData(accountName) {
        console.groupCollapsed('Account id:', this.id)
        console.table(accountName)
        console.groupEnd()
    }
}
