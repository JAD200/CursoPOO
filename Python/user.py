from account import Account

class User(Account):
    id          = int
    email       = str
    password    = str

    def __init__(self, id, name, document, email, password):
        super(User, self).__init__(name, document)
        self.id = id
        self.email = email
        self.password = password