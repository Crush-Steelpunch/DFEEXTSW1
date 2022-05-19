# Budget App

Goal: Create a Budget class that can instantiate objects
based on different budget categories like food, clothing, and entertainment.

The class should have an attribute for the category balance. 
The class should have methods for withdrawing, depositing and 
transfering the balance.

## Decomposition - Split into smaller tasks

- Create a Budget Class
  - create objects from it
- Create attribute
  - balance
- Create methods
  - deposit
    - add a value to the balance attribute
  - withdraw
    - subtract a value from the balance attribute
  - transfer
    - subtract from object balance and add to a different object balance attribute.

## Pattern Matching


- Create a Budget Class    `class Budget:`
  - create objects from it
- Create attribute
  - balance: Either, have a static attribute, or create the attribute on object creation
    - use an `__init__` method?

- Create methods
  - deposit
    `def deposit(self, amount):`
    - add a value to the balance attribute
        `self.balance = self.balance + amount`
  - withdraw
    `def withdraw(self, amount)`
    - subtract a value from the balance attribute
        `self.balance = self.balance - amount`
  - transfer
    `def transfer(self, amount, otherobjectref)`
    - subtract from object balance and add to a different object balance attribute.
        `self.balance = self.balance - amount`
        `otherobjectref.balance = otherobjectref.balance + amount`
      - OR
        `self.withdraw(amount)`
        `otherobjectref.deposit(amount)`

## Algorithmic Thinking

- flowchart or psudocode

## Write the code

```python
class Budget:

    def __init__(self,startingbalance=0):
        self.balance = startingbalance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
```
