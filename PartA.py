class House:
    def __init__(self, house_number, street, area, num_beds, price):
        self.house_number = house_number
        self.street = street
        self.area = area
        self.num_beds = num_beds
        self.price = price
    
    def print_attributes(self):
        print(f"House Number: {self.house_number}, Street: {self.street}, Area: {self.area}, Beds: {self.num_beds}, Price: {self.price}")
    
    def update_house_number(self, new_number):
        if isinstance(new_number, int):
            self.house_number = new_number 
    
    def update_street(self, new_street):
        if isinstance(new_street, str):
            self.street = new_street
    
    def update_area(self, new_area):
        if isinstance(new_area, str):
            self.area = new_area
    
    def update_num_beds(self, new_beds):
        if isinstance(new_beds, int):
            self.num_beds = new_beds
    
    def update_price(self, new_price):
        if isinstance(new_price, (int, float)):
            self.price = new_price

class Apartment(House):
    def __init__(self, house_number, street, area, num_beds, price, floor, has_elevator):
        super().__init__(house_number, street, area, num_beds, price)
        self.floor = floor
        self.has_elevator = has_elevator
    
    def print_attributes(self):
        super().print_attributes()
        print(f"Floor: {self.floor}, Elevator: {self.has_elevator}")
    
    def update_floor(self, new_floor):
        if isinstance(new_floor, int):
            self.floor = new_floor
    
    def update_has_elevator(self, new_elevator):
        if isinstance(new_elevator, bool):
            self.has_elevator = new_elevator

#instances
house = House(123, "Casta", "Latchford", 3, 250000)
apartment = Apartment(456, "Castle", "Field", 2, 180000, 5, True)

#calling methods
house.print_attributes()
apartment.print_attributes()

#updating attributes
house.update_price(260000)
house.update_num_beds(4)
print("\nAfter Updates:")
house.print_attributes()
apartment.update_floor(6)
apartment.update_has_elevator(False)
apartment.print_attributes()
