class Car:
    brand = "Toyota" 
    
    def __init__(self, brand=None):
        if brand:
            self.brand = brand
    
    def start(self):
        print(f"The {self.brand} car is starting...")

if __name__ == "__main__":
    car1 = Car()
    print(f"Car 1 brand: {car1.brand}")  
    car1.start() 
    
    car2 = Car("Honda")
    print(f"Car 2 brand: {car2.brand}")
    car2.start()  
    
    car1.brand = "BMW"
    print(f"Car 1 new brand: {car1.brand}")
    car1.start() 