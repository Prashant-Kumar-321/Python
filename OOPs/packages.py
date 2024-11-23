from datetime import datetime

class Package: 
    def __init__(self, number, sender, recipient, weight, ordered_date, shipping_date): 
        self.number = number 
        self.sender = sender 
        self.recipient = recipient 
        self.weight = weight
        self.ordered_date = ordered_date
        self.shipping_date = shipping_date
    
    def __str__(self): 
        return f"Package {self.number}, {self.sender} to {self.recipient}, {self.weight}Kg"

    def calculate_shiping_cost(self, cost_per_kg): 
        return self.weight * cost_per_kg 

    def remaining_days_for_shipping(self): 
        now = datetime.now()

        if (now > self.shipping_date): 
            return f"Package {self.number} has been delivered"
        
        dt = self.shipping_date - now 

        return f"Packages {self.number} will be delivered within {dt.days} days"




    

def main(): 
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10, ordered_date=datetime(2024, 11, 21), shipping_date=datetime(2024, 12, 9)),
        Package(number=3, sender="Bob", recipient="Charlie", weight=20, ordered_date=datetime(2023, 6, 10), shipping_date=datetime(2023, 6, 16)),
    ]

    for package in packages: 
        print(f"{package} costs RS {package.calculate_shiping_cost(12)}")
        print(package.remaining_days_for_shipping())

if __name__ == "__main__": 
    main()