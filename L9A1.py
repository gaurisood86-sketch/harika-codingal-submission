class nike:
    def __init__ (self , type , model , price , color):
        self.type=type
        self.model=model
        self.price=price
        self.color=color

    def authentification(self):
        print("This is a Nike Product ")

    def details(self):
        print(f"This is a {self.model} {self.type} and is {self.color} color . It's price is {self.price}")

nikeshoe=nike("AIR JORDANS" , "SHOE" , "BLACK" , "250$")
niketshirt=nike("MARVELS" , "TSHIRT" , "BLUE" , "50$")

nikeshoe.authentification()
nikeshoe.details()
niketshirt.authentification()
niketshirt.details()