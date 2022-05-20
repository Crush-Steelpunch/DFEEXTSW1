class Budget:

    def __init__(self,startingbalance=0):
        self._balance = startingbalance
    
    def deposit(self, amount):
        self._balance = self._balance + amount
    
    def withdraw(self, amount):
        self._balance = self._balance - amount

    def transfer(self, amount, otherobjectref):
#        self.balance = self.balance - amount
#        otherobjectref.balance = otherobjectref.balance + amount
        self.withdraw(amount)
        otherobjectref.deposit(amount)

# Create some objects on catagories

food = Budget(30)
clothes = Budget(100)
entertainment = Budget(50)
pets = Budget(30)
gardening = Budget(5)


print("====check balances====")
print("food balance: " + str(food._balance))
print("clothes balance: " + str(clothes._balance))
print("entertainment balance: " + str(entertainment._balance))

print("====test deposit and withdraw====")
food.deposit(10)
print("food balance: " + str(food._balance))
clothes.withdraw(30)
print("clothes balance: " + str(clothes._balance))
entertainment.withdraw(40)
print("entertainment balance: " + str(entertainment._balance))


print("=== transfer balance from clothes to entertainment ===")
clothes.transfer(40, entertainment)
print("clothes balance: " + str(clothes._balance))
print("entertainment balance: " + str(entertainment._balance))

clothes._balance = 1000
print(clothes._balance)