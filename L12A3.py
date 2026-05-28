import math
class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        """Template method for area calculation."""
        raise NotImplementedError("Subclasses must implement this method.")

    def calculate_perimeter(self):
        """Template method for perimeter calculation."""
        raise NotImplementedError("Subclasses must implement this method.")

    def display_info(self):
        print(f"Shape: {self.name} | Area: {self.calculate_area():.2f} | Perimeter: {self.calculate_perimeter():.2f}")
