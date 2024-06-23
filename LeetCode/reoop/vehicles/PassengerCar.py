from BaseVehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450

    def __init__(self, brand, model, license_plate_number):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage: float):
        percentage = int(mileage / self.MAX_MILEAGE * 100)
        self.battery_level -= percentage
