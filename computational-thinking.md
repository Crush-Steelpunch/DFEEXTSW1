# Decomposition

Split the problem in to small chunks 

```
Write a Python function to find the Max of three numbers
```

- Write a function
- Three numbers
  - function needs to take three numbers
- Find the maximum


# Pattern Matching

What coding tools do I know that answer the problem?

- Write a function
    `def func(var):`

- Three numbers, my function needs to have 3 input vars
    `def func(var1,var2,var3):`
- Find the maximum, 
    - This sounds like a test!
    - Maybe use an if statement
    ` if var1 > var2:`

Problem! if statements can only test two objects at a time
- Maybe iterate? for loop?
- Maybe just run a series of tests?
   - nested if statment?


# Algorithmic Thinking
How do I take these small chunks and make a program?

- Use Flowcharts
- Use Psudocode

example psudocode
```
BEGIN
INPUT var1 var2 var3
TEST is VAR1 > var2
    TEST is VAR1 > var3
    TEST is VAR2 > var3
OUTPUT VARx
```

# Write the program

```python
def maxofthree(var1, var2, var3):
    if var1 > var2:
        if var1 > var3:
            return var1
        else:
            return var3
        if var2 > var3:
            return var2
        else:
            return var3

print(maxofthree(12,25,256))
```


# Links

[BBC Bitesize](https://www.bbc.co.uk/bitesize/guides/zp92mp3/revision/1)