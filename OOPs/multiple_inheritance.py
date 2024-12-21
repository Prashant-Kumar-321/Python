class Rechargeable: 
    def __init__(self, battery_capacity): 
        self.battery_capacity = battery_capacity # in mAh
    
    def charge(self): 
        print(f"Charging... Battery capacity: {self.battery_capacity} mAh.")

class Communicable: 
    def __init__(self, communication_technology): 
        self.communication_technology = communication_technology # wifi, bluetooth, etc 
    
    def communicate(self): 
        print(f"Communicating via: {self.communication_technology}.")
    

class SmartPhone(Rechargeable, Communicable): 
    def __init__(self, battery_capacity, communication_technology, brand, model): 
        Rechargeable.__init__(self, battery_capacity) 
        Communicable.__init__(self, communication_technology)

        self._brand = brand 
        self.model = model 
    
    @property 
    def brand(self):
        return self._brand 
    
    @brand.setter
    def brand (self, newValue): 
        self._brand = newValue 

    
    def show_details(self): 
        print(f"Smart phone : {self.brand} {self.model}")
        print(f"Battery: {self.battery_capacity}mAh, Communication: {self.communication_technology}")


def main(): 
    smartphone = SmartPhone(4000, "WiFi", "iPhone", "14 max pro") 
    smartphone.brand = "Iphone"
    print(smartphone.brand)
    # smartphone.show_details()
    # smartphone.charge()



if __name__ == "__main__": 
    main() 
