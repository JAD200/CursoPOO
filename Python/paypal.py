from payment import Payment

class Paypal(Payment):
    email = str

    def __init__(id, email):
        super(Paypal, self).__int__(id)
        self.email = email