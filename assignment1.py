# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Derived class
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        # Call parent constructor
        super().__init__(brand, model)
        self.os = os
        self.storage = storage
    
    def make_call(self, number):
        return f"Calling {number} from {self.device_info()}..."
    
    def install_app(self, app):
        return f"{app} installed on {self.device_info()} with {self.os}."

# Another derived class
class Tablet(Device):
    def __init__(self, brand, model, stylus_support):
        super().__init__(brand, model)
        self.stylus_support = stylus_support
    
    def draw(self):
        return f"Drawing on {self.device_info()} with stylus support: {self.stylus_support}"
    

# Example objects
phone1 = Smartphone("Samsung", "Galaxy S24", "Android", "256GB")
tab1 = Tablet("Apple", "iPad Pro", True)

print(phone1.make_call("0712345678"))
print(phone1.install_app("Instagram"))
print(tab1.draw())