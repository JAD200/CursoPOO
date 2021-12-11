from car import Car

class UberVan(Car):
    typeCarAccepted = []
    seatMaterail = []

    def __init__(self, license, driver,typeCarAccepted, seatMaterail):
        super(UberVan,self).__init__(license,driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatMaterail = seatMaterail
