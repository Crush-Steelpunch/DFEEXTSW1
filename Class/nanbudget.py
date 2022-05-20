#ategoryBalance class 
# attribute  category balance(food, clothing, and entertainment.)
# methods withdrawing, depositing and transfering 
class Budget:  
    categoryBalance= 0   
    store={}
    def __init__(self,food, clothing,entertainment):   
        self.entertainment = entertainment   
        self.food = food    
        self.clothing= clothing
        self.store={"food":food,"clothing":clothing,"entertainment":entertainment}
    def withdraw(self):
        money=input(" Money you want to withdraw ")
        type=input(" which type ")
        typeMoney=self.store[type]
        money=int(money)
        self.store[type]=typeMoney-money
        print(self.store)
if __name__ == "__main__":
        b=Budget(70,100,100)
        b.withdraw()