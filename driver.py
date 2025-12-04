from person import Person
from license import License
class Driver(Person):
    def __init__(self, name, age, CNIC, license: License, phone_num, company_name, driver_id):
        super().__init__(name, age, CNIC)
        self.license = license
        self.driver_id = driver_id
        self.phone_num = phone_num
        self.company_name = company_name

    def __str__(self):
        return (f"{self.name} has a license {self.license.license_num} "
                f"and is a certified driver for {self.company_name} "
                f"with the driver id of {self.driver_id}")

    def driving(self):
        return f"{self.name} with the driver id {self.driver_id} is driving right now"