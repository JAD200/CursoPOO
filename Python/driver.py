from account import Account

class Driver(Account):
    id          = int
    email       = str
    password    = str

    def __init__(self, id, name, document, email, password):
        super(Driver, self).__init__(name, document)
        self.id = id
        self.email = email
        self.password = password