class Driver extends Account {
    constructor(id, name, document, email, password) {
        super(name, document);
        this.id = id;
        this.email = email;
        this.password = password;
    }
}