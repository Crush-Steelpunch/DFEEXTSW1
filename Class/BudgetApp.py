class Budget:

    def __init__(self,startingbalance=0):
        self.balance = startingbalance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdraw(self, amount):
        self.balance = self.balance - amount

    def transfer(self, amount, otherobjectref):
#        self.balance = self.balance - amount
#        otherobjectref.balance = otherobjectref.balance + amount
        self.withdraw(amount)
        otherobjectref.deposit(amount)

# Create some objects on catagories

food = Budget(30)
clothes = Budget(100)
entertainment = Budget(50)

print("====check balances====")
print("food balance: " + str(food.balance))
print("clothes balance: " + str(clothes.balance))
print("entertainment balance: " + str(entertainment.balance))

print("====test deposit and withdraw====")
food.deposit(10)
print("food balance: " + str(food.balance))
clothes.withdraw(30)
print("clothes balance: " + str(clothes.balance))
entertainment.withdraw(40)
print("entertainment balance: " + str(entertainment.balance))


print("=== transfer balance from clothes to entertainment ===")
clothes.transfer(40, entertainment)
print("clothes balance: " + str(clothes.balance))
print("entertainment balance: " + str(entertainment.balance))