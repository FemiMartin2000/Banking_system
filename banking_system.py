#parent class
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender=gender
    def show_user_details(self):
        print("personal details")
        print("Name",self.name)
        print("Age",self.age)
        print("Gender",self.gender)


#Child class
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name, age,gender)
        self.balance=0
    def depoist(self,amount):
        self.balance=self.balance + amount
        print("account balance has been updated to",self.balance)
    def withdrawal(self,amount):

        if (amount>self.balance):
            print('Insuffient balance')
        else:
            self.balance = self.balance - amount
            print("Account balance has been updated to ", self.balance)
    def view_balance(self):
        self.show_user_details()
        print("Account balance has been updated to  ", self.balance)



Femi = Bank('Femi',22,"F")
Femi.depoist(700)
Femi.depoist(700)
Femi.withdrawal(300)
Femi.view_balance()
