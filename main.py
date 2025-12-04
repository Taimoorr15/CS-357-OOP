from person import Person
from license import License
from driver import Driver
from car import Car

def main():
    # Create a license
    license1 = License(12345, "HTV", "2028-12-31")

    # Create a driver with license (composition) + person info
    driver1 = Driver("Ali", 30, "42101-1234567-8", license1, "03121234567", "Uber", "DRV001")

    # Create a car
    car1 = Car("Civic", "Honda", "Sedan")

    # Display details
    print(driver1)                # driver details
    print(driver1.license)        # license details
    print(car1)                   # car details
    print(driver1.driving())      # driving action
    print(car1.is_moving())       # car action

if __name__ == "__main__":
    main()
