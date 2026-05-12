class amount:
    def __init__ (self , bal , acc):
        self.balence=bal
        self.account_no=acc

    def debit (self , amount):
        self.balence=self.balence - amount
        print("Rs" , amount , "from account no ", self.account_no , "was debited")
        print("Total balence = " , self.get_bal())

    def credit(self , amount):
        self.balence=self.balence + amount
        print("Rs" , amount , "from account no" , self.account_no , "was credited")
        print("Total balence =" , self.get_bal())

    def get_bal(self):
        return self.balence
    
account1=amount(10000 , 12220)
account1.debit(4000)
account1.credit(3000)


    

