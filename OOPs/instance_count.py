class Product: 
    _instance_count = 0
    @classmethod 
    def increment_instance_count(cls): 
        cls._instance_count += 1
    
    @classmethod 
    def instance_count(cls): 
        return cls._instance_count

    def __init__(self, name, cost):
        self.name = name 
        self.cost = cost 
        Product.increment_instance_count()
    
    def __str__(self): 
        return f"{self.name}, Rs {self.cost}"


def main(): 
    print(Product.instance_count())
    product_list = []
    for _ in range(10): 
        product_list.append(Product("name", 120))
    
    print(Product.instance_count())


if __name__ == "__main__": 
    main()