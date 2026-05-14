from abc import ABC , abstractmethod

class Vehical(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehical):
    def start_engine(self):
        print("the car has started. vroom vroom")

    def stop_engine(self):
        print("the car haas stopped.")


class Bike(Vehical):
    def start_engine(self):
        print("the bike has started. wohooo")


car1=Car()
car1.start_engine()
car1.stop_engine()
bike1=Bike()
bike1.start_engine()
