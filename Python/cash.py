from payment import Payment

class Cash(Payment):
    def __init__(self,id):
        super(Cash, self).__init__(id)